from term_frequency_summarizer import TFSummarizer
from cosine_distance_summarizer import CosineDistanceSummarizer

def get_summary(text, reduction_percent=0.5):
    return CosineDistanceSummarizer().get_summary(text, reduction_percent, ordered=True)

if __name__ == '__main__':
    print(get_summary("Facebook CEO Mark Zuckerberg held an extended conference with employees today, addressing accusations that Facebook \
        allowed election misinformation and veiled promotions of violence from President Donald Trump. While Zuckerberg said he should have \
        offered more transparency to employees, he stood by what he called a “pretty thorough” evaluation of Trump’s posts, saying the choice \
        to avoid labeling or removing them was difficult but correct. According to a recording obtained by The Verge, Zuckerberg described \
        being upset by Trump’s recent posts, one of which warned protesters that “when the looting starts, the shooting starts.” But “I knew \
        that I needed to separate out my personal opinion ... from what our policy is and the principles of the platform we’re running are — \
        knowing that the decision that we made was going to lead to a lot of people being very upset inside the company and a lot of the media\
        criticism we’re going to get,” said Zuckerberg. “Likely this decision has incurred a massive practical cost for the company to do what \
        we think is the right step.” Facebook has followed a different path from Twitter, which fact-checked two Trump tweets about voting and \
        restricted the protest comments for “glorifying violence.” And Zuckerberg’s decision has proven controversial among employees, some of \
        whom staged a virtual walkout on Monday in protest. Echoing comments made last week, Zuckerberg said the choice upheld Facebook’s \
        dedication to free expression. “The presumption on our service is that you should be able to say what you want unless you’re causing\
        a specific harm and we enumerate what the harms are and try to enforce them. And I do think that default is right,” he said."))



    

