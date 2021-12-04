from flask import Flask
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, SubmitField
from wtforms.validators import Optional
from flask_bootstrap import Bootstrap
from twitter_scrapper import fetch_data


class RequestForm(FlaskForm):
    words = StringField('Words', validators=[Optional()])
    exacts = StringField('Exacts', validators=[Optional()])
    from_date = DateField('From', validators=[Optional()])
    until_date = DateField('Until', validators=[Optional()])
    submit = SubmitField('Scrape!')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request', methods=['GET', 'POST'])
def form():
    form = RequestForm()
    if form.validate_on_submit():
        dict_form = {"words": f'{form.words.data}', "exacts": f'{form.exacts.data}',
                     "from_date": f'{form.from_date.data}', "until_date": f'{form.until_date.data}'}
        fetch_data(dict_form)
        return redirect('/results')
    return render_template('request.html', form=form)


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run()
