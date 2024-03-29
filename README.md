# TwitterScrapper-SentimentAnalysis
Use Twitter's API to make specific requests on special events, analyse the data collected via sentiment analysis algorithms and display it on a Flask web app that runs locally.

### How to run the Flask app ?

1. You first need to create a [Twitter Developer Account](https://developer.twitter.com/en) to be able to pull tweets
2. Create your app on the developer portal and retreive your credentials (especially the bearer_token)
3. Create a local variable for your BEARER_TOKEN with the command

    ` export BEARER_TOKEN=Your token `

4. Get a secret key for your FLASK application init file

    ` import os `
    
    ` os.urandom(12) `
    
5. Install the dependences for only running the app

    ` pip3 install flask flask_wtf requests pandas nltk autocorrect sklearn`
    
6. Install Spacy using this [link](https://spacy.io/usage)

7. Install ChartJS for the visualization part

    ` npm install chart.js `

8. If you want to contribute you need to retrieve [Kaggle dataset](https://www.kaggle.com/datasets/kazanova/sentiment140) 

9. Run the command
    
    ` python3 run.py `

### A quick video to show how the app works



https://user-images.githubusercontent.com/71345328/182701935-1c0871f1-5435-4220-94bd-b3c361243f65.mov

