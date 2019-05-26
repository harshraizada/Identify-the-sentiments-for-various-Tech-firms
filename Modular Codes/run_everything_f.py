import pandas as pd
import numpy as np
import joblib
from preprocessing_functions import preprocessing


def sent_analyzer(tweet):
    """Analyzing sentiments in tweet
    Parameters:
    ----------
    tweet : Tweets by users using curl command (a list of strings)

    Returns:
    -------
    Wether the sentiment behind the tweet is Negative or Positive will show on clients terminal"""
    # reading tweets
    tweet_series = pd.Series(tweet)
    # Preprocessing the tweets for vectorization
    pp = preprocessing(tweet_series)
    # Loading the vectorizer
    vectorizer = joblib.load('bow_vectorizer')
    # Transforming the tweets into vectors
    pp_vec = vectorizer.transform(pp)
    # Loading the trained Logistic Regression Model
    model = joblib.load('Trained SA LR model')
    # Predicting the sentiments from tweets
    pred = model.predict(pp_vec)
    for value in pred:
        if value == 0:
            print("It's a Positive Comment:)")
        else:
            print("It's a Negative Comment: (")
    return
