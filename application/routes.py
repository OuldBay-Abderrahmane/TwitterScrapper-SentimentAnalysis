from application import app, db
from flask import render_template, redirect
from application.form import RequestForm, DataStore
from application.models import Results
import json

import application.twitter_scrapper as scrp
from application.scripts.analysis import get_data
from flask_bootstrap import Bootstrap


data = DataStore()

Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request', methods=['GET', 'POST'])
def form():
    form = RequestForm()
    if form.validate_on_submit():
        data.words = form.words.data
        data.exacts = form.exacts.data
        
        scrp.fetch_data(data)
        result = get_data()
        entry = Results(positive_count = result[0][0], positive_reviews = result[2], negative_reviews = result[1], data = result[3])
        db.session.add(entry)
        db.session.commit()
        
        return redirect('/results')
    return render_template('request.html', form=form)


@app.route('/results')
def results():
    sentiments = db.session.query(Results.positive_count).all()
    sentiments = (int.from_bytes(sentiments[0][0], byteorder='little'))
    sentiments_neg = 100 - sentiments
    print(sentiments_neg, sentiments)
    positive, negative = db.session.query(Results.positive_reviews).all()[0][0], db.session.query(Results.negative_reviews).all()[0][0]

    return render_template('results.html', sentiment = sentiments, sentimentNeg = sentiments_neg, positive=positive, negative=negative )

@app.route('/restart', methods=['POST'])
def restart():
    db.drop_all()
    db.create_all()
    return redirect('/request')


@app.before_request
def create_tables():
    db.create_all()

