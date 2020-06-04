from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import SubmitWebsiteForm, SubmitTextForm
import os
from text_summarizer import get_summary
from scrape import get_string_contents_from_url

app = Flask(__name__, static_folder='static',)
app.config['SECRET_KEY'] = os.environ['SOME_SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
def home():
    website_form = SubmitWebsiteForm()
    text_form = SubmitTextForm()

    if website_form.validate_on_submit():
        website_url = website_form.websiteUrl.data
        dict = scrape(website_url)

        summary_dict = {}
        for header, p in dict.items():
            summary_dict[header] = get_summary(p)

        context = {'summary_dict': summary_dict}
        return render_template('home.html', website_form=website_form, text_form=text_form, context=context)

    if text_form.validate_on_submit():
        text = text_form.text.data
        summary = get_summary(text)
        summary_dict = {'Summary': summary}
        context = {'summary_dict': summary_dict}

        # Calculate time saved by summary
        minutes_before = estimate_reading_time(text)
        minutes_after = estimate_reading_time(summary)
        minutes_saved = round(minutes_before - minutes_after)

        reduction_percentage = 100 * (len(text) - len(summary)) / len(text)
        context['reduction_percentage'] = round(reduction_percentage)

        # Only show UI if time saved is substantial
        if minutes_saved > 1:
            context['minutes_saved'] = minutes_saved

        return render_template('home.html', website_form=website_form, text_form=text_form, context=context)

    return render_template('home.html', website_form=website_form, text_form=text_form)


@app.route('/scrape/<path:websiteUrl>')
def scrape(websiteUrl):
    return get_string_contents_from_url(websiteUrl)


def estimate_reading_time(text):
    # Based on research done in this field, people are able to read English at 200 WPM on paper,
    # and 180 WPM on a monitor (the current record is 290 WPM).
    WPM = 180
    WORD_LENGTH = 5
    total_words = count_words_in_text(text, WORD_LENGTH)
    return total_words / WPM


def count_words_in_text(text, word_length):
    total_words = 0
    total_words += len(text) / word_length
    return total_words


# This condition is only true if we run the script directly
# This helps avoid using environment variables
# This way you can run the app by using 'python flaskproject.py'
if __name__ == '__main__':
    app.run(debug=True)
