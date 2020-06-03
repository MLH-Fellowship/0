import spacy

nlp = spacy.load("en_core_web_lg")

class TFSummarizer(object):

    def get_summary(self, text, reduction_percent, ordered=False):
        doc = nlp(text.lower())
        sentences = list(doc.sents)

        num_sentences = int(round(len(list(doc.sents))*(1-reduction_percent)))
        tokenFreq = self._calculate_term_frequency(doc)
        sentenceScore = self._rank_sentences(doc, tokenFreq)

        summarizedText = ""
        if ordered:
            sentenceScore = sentenceScore[:num_sentences]
            for sent in sentences:
                if sent in sentenceScore:
                    summarizedText += "{} ".format(str(sent))
        else:
            for i in range(min(num_sentences, len(sentenceScore))): 
                summarizedText += str(sentenceScore[i])
        
        return summarizedText

    def _calculate_term_frequency(self, doc):
        tokenFreq = {}
        desiredPOS = ['PROPN', 'VERB', 'NOUN', 'ADJ']
        for token in doc:
            if (token.text not in nlp.Defaults.stop_words) and (token.pos_ in desiredPOS):
                if token.text in tokenFreq.keys():
                    tokenFreq[token.text] += 1
                else:
                    tokenFreq[token.text] = 1
        maxFreq = max(tokenFreq.values())
        tokenFreq.update((k, v/maxFreq) for k,v in tokenFreq.items())
        return tokenFreq

    def _rank_sentences(self, doc, tokenFreq):
        sentenceStrength = {}
        for sentence in doc.sents:
            for word in sentence:
                if str(word) in tokenFreq.keys():
                    if sentence in sentenceStrength.keys():
                        sentenceStrength[sentence] += tokenFreq[str(word)]
                    else:
                        sentenceStrength[sentence] = tokenFreq[str(word)]
        return [k for k, _ in sorted(sentenceStrength.items(), key=lambda item:item[1], reverse=True)]