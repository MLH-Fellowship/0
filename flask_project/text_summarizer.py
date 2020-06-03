from term_frequency_summarizer import TFSummarizer
from cosine_distance_summarizer import CosineDistanceSummarizer

def get_summary(text, reduction_percent=0.5):
    return CosineDistanceSummarizer().get_summary(text, reduction_percent, ordered=True)

if __name__ == '__main__':
    print(get_summary("Cats are amazing animals. They have fur and they purr. Very cool"))



    

