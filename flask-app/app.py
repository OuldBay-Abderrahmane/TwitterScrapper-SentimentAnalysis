from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


app = Flask(__name__)
app.from_object(Config)


class RequestForm(FlaskForm):
    words = StringField('Username', validators=[DataRequired()])
    exacts = PasswordField('Password')
    from_date = DateField('Date')
    until_date = DateField('Date')
    submit = SubmitField('Sign In')


@app.route("/")
@app.route("/index")
def hello_world():
    return render_template("base.html")


@app.route('/request')
def request():
    form = RequestForm()
    return render_template('requests.html', title='Request', form=form)
