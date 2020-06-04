import spacy
import numpy as np

nlp = spacy.load("en_core_web_lg")

class CosineDistanceSummarizer(object):
    """
    Class to summmarize text based on text rank.
    """

    def get_summary(self, text, reduction_percent, vector_type="occurance", ordered=False):
        """
        Function to produce text summary. 

        Parameters:
            text (str): Text to convert to summary.
            reduction_percent (float): Decimal representation of how much text to reduce (i.e. 0.5 = 50%).
            vector_type(str): Type of sentence vector to use. Options: "occurance" or "glove".
            ordered (bool): Set to true if summary should retain sentence order from text. Default is False.
        Returns:
            summary (str): A summary of text. 
        """
        doc = nlp(text.lower())
        sentences = list(doc.sents)
        num_sentences = int(round(len(sentences)*(1-reduction_percent)))

        matrix = self._create_cosine_similarity_matrix(sentences, vector_type)
        ranking = np.argsort(-np.sum(matrix, axis=0))
        ordered_ranking = sorted(ranking[:num_sentences])

        summary = ""
        for i in range(num_sentences):
            if ordered:
                summary += self._format_sentence(sentences[ordered_ranking[i]]) 
            else:
                summary += self._format_sentence(sentences[ranking[i]])
        return summary

    def _create_cosine_similarity_matrix(self, sentences, vector_type):
        numSentences = len(sentences)
        matrix = np.zeros((numSentences, numSentences))
        for i in range(numSentences):
            for j in range(numSentences):
                if i != j: 
                    if vector_type == "occurance":
                        matrix[i][j] = self._cosine_similarity_occurance(sentences[i], sentences[j])
                    else:
                        matrix[i][j] = self._cosine_similarity_word2vec(sentences[i], sentences[j])
        return matrix

    def _cosine_similarity_word2vec(self, sent1, sent2):
        if sent1.has_vector and sent2.has_vector:
            return sent1.similarity(sent2)
    
    def _cosine_similarity_occurance(self, sent1, sent2):
        desiredPOS = ['PROPN', 'VERB', 'NOUN', 'ADJ']
        all_words = []
        for token in sent1:
            if token.text not in all_words:
                all_words.append(token.text)
        for token in sent2:
            if token.text not in all_words:
                all_words.append(token.text)
        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        for token in sent1:
            if token.pos_ in desiredPOS:
                vector1[all_words.index(token.text)] += 1
    
        for token in sent2:
           if token.pos_ in desiredPOS:
                vector2[all_words.index(token.text)] += 1
    
        return (np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
    
    def _format_sentence(self, sentence):
        stringSentence = ""
        for i, word in enumerate(sentence):
            if word.pos_ == 'PROPN' or i == 0:
                stringSentence += word.text_with_ws.title()
            else:
                stringSentence += word.text_with_ws
        return stringSentence