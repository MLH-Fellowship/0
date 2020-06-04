from term_frequency_summarizer import TFSummarizer
from cosine_distance_summarizer import CosineDistanceSummarizer

def get_summary(text, reduction_percent=0.5):
    """
    Function to produce text summary. 

    Parameters:
        text (str): Text to convert to summary.
        reduction_percent (float): Decimal representation of how much text to reduce (i.e. 0.5 = 50%). Default is 0.5.
    Returns:
        summary (str): A summary of text. 
    """
    return CosineDistanceSummarizer().get_summary(text, reduction_percent, ordered=True)

if __name__ == '__main__':
    print(get_summary("Cats are amazing animals. They have fur and they purr. Very cool"))



    

