from term_frequency_summarizer import TFSummarizer

def get_summary(text, num_sentences=3):
    return TFSummarizer().get_summary(text, num_sentences)

if __name__ == '__main__':
    print(get_summary("Here is a lot of text about not very much. I do like cats. Cats have a lot of fur. They purr when they're happy.", 1))



    

