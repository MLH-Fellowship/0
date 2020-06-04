from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, URL, Length


class SubmitWebsiteForm(FlaskForm):
    websiteUrl = URLField('Summarize from Website',
                          validators=[DataRequired(), URL()], description="test")
    submit = SubmitField('Go')


class SubmitTextForm(FlaskForm):
    text = TextAreaField('Text', validators=[
        DataRequired(), Length(min=150)])
    submit = SubmitField('Go')
