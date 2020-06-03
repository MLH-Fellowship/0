from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, URL


class SubmitWebsiteForm(FlaskForm):
    websiteUrl = URLField('Website', validators=[DataRequired(), URL()])
    submit = SubmitField('Go')
