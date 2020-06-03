import spacy
import numpy as np

nlp = spacy.load("en_core_web_lg")

class CosineDistanceSummarizer(object):

    def get_summary(self, text, reduction_percent):
        doc = nlp(text.lower())
        sentences = list(doc.sents)
        num_sentences = int(round(len(sentences)/(1-reduction_percent)))

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
                    matrix[i][j] = self._cosine_similarity(sentences[i], sentences[j])
        return matrix

    def _cosine_similarity(self, sent1, sent2):
        if sent1.has_vector and sent2.has_vector:
            return sent1.similarity(sent2)