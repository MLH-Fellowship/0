import spacy
import numpy as np

nlp = spacy.load("en_core_web_lg")

class CosineDistanceSummarizer(object):

    def get_summary(self, text, reduction_percent):
        doc = nlp(text.lower())
        sentences = list(doc.sents)
        num_sentences = int(round(len(sentences)*(1-reduction_percent)))

        matrix = self._create_cosine_similarity_matrix(sentences)
        ranking = np.argsort(np.sum(matrix, axis=0))

        summary = ""
        for i in range(num_sentences):
            summary += str(sentences[ranking[i]])
        return summary

    def _create_cosine_similarity_matrix(self, sentences):
        numSentences = len(sentences)
        matrix = np.zeros((numSentences, numSentences))
        for i in range(numSentences):
            for j in range(numSentences):
                if i != j: 
                    a = self._cosine_similarity_occurance(sentences[i], sentences[j])
                    matrix[i][j] = a
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