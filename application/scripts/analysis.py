from ntpath import join
import pandas as pd
import json
from joblib import load
import application.scripts.preprocessing as pp

def get_data():

    with open('application/scripts/tweets.json') as f:
        data = json.load(f)
    data = pd.DataFrame(data["data"])
    
    clf = load('application/scripts/model.joblib') 

    result = []
    negative_comments = ''
    positive_comments = ''

    for text in data.text:
        clean_data = pp.cleaned_data(text)
        prediction = clf.predict([clean_data])
        result.append(prediction)
        lemma = pp.lemmatize(clean_data)
        if prediction == 0:
            negative_comments = negative_comments + lemma
        else:
            positive_comments = positive_comments + lemma

    from collections import Counter

    split_it_negative = negative_comments.split()
    split_it_positive = positive_comments.split()

    counter_negative = Counter(split_it_negative).most_common(12)
    counter_positive = Counter(split_it_positive).most_common(12)
    
    counter_negative = ", ".join("(%s, %s)" % tup for tup in counter_negative)
    counter_positive = ", ".join("(%s, %s)" % tup for tup in counter_positive)
    count_positive = sum(result)
    return [count_positive, counter_negative, counter_positive, json.dumps("application/scripts/tweets.json", ensure_ascii=False) ]


