from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import SubmitWebsiteForm, SubmitTextForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SOME_SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
def home():
    website_form = SubmitWebsiteForm()
    if website_form.validate_on_submit():
        return f'Success! Now parse the web data from {website_form.websiteUrl.data}'

    text_form = SubmitTextForm()
    if text_form.validate_on_submit():
        return f'Success! Now summarize from text {text_form.text.data}'

    return render_template('home.html', website_form=website_form, text_form=text_form)


@app.route('/summarize')
def summarize():
    return 'Hello world'


# This condition is only true if we run the script directly
# This helps avoid using environment variables
# This way you can run the app by using 'python flaskproject.py'
if __name__ == '__main__':
    app.run(debug=True)
