from flask import Flask, escape, request, render_template, url_for, flash, redirect
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SOME_SECRET_KEY']


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/summarize')
def summarize():
    return 'Hello world'


# This condition is only true if we run the script directly
# This helps avoid using environment variables
# This way you can run the app by using 'python flaskproject.py'
if __name__ == '__main__':
    app.run(debug=True)
