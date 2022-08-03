from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import Optional


class RequestForm(FlaskForm):
    words = StringField('Words', [validators.DataRequired()])
    exacts = StringField('Exacts', validators=[Optional()])
    submit = SubmitField('Scrape!')

class DataStore:
    words = None
    exacts = None

