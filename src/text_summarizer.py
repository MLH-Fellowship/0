import spacy

nlp = spacy.load("en_core_web_lg")

def get_summary(text, num_sentences=3):
    doc = nlp(text.lower())
    tokenFreq = _calculate_term_frequency(doc)
    sentenceScore = _rank_sentences(doc, tokenFreq)

    summarizedText = ""
    for i in range(min(num_sentences, len(sentenceScore))): 
        summarizedText += str(sentenceScore[i])
    
    return summarizedText


def _calculate_term_frequency(doc):
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

def _rank_sentences(doc, tokenFreq):
    sentenceStrength = {}
    for sentence in doc.sents:
        for word in sentence:
            if str(word) in tokenFreq.keys():
                if sentence in sentenceStrength.keys():
                    sentenceStrength[sentence] += tokenFreq[str(word)]
                else:
                    sentenceStrength[sentence] = tokenFreq[str(word)]
    return [k for k, _ in sorted(sentenceStrength.items(), key=lambda item:item[1], reverse=True)]

if __name__ == '__main__':
    print(get_summary("Here is a lot of text about not very much. I do like cats. Cats have a lot of fur. They purr when they're happy.", 1))



    

