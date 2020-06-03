from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import SubmitWebsiteForm, SubmitTextForm
import os
from text_summarizer import get_summary
from scrape import get_string_contents_from_url

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SOME_SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
def home():
    website_form = SubmitWebsiteForm()
    if website_form.validate_on_submit():
        return f'Success! TODO: Now parse the web data from {website_form.websiteUrl.data}'

    text_form = SubmitTextForm()
    if text_form.validate_on_submit():
        text = text_form.text.data
        summary = get_summary(text)
        return f'Text summary: {summary}'

    return render_template('home.html', website_form=website_form, text_form=text_form)


@app.route('/scrape/<path:websiteUrl>')
def scrape(websiteUrl):
    return get_string_contents_from_url(websiteUrl)


# This condition is only true if we run the script directly
# This helps avoid using environment variables
# This way you can run the app by using 'python flaskproject.py'
if __name__ == '__main__':
    app.run(debug=True)
