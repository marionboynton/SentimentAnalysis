# UPDATE: this is the path were the models are stored
path = "./"

from preprocessing import preprocess
from scraper import scrape

# IMPORT
KERAS_MODEL = "model.h5"
WORD2VEC_MODEL = "model.w2v"
TOKENIZER_MODEL = "tokenizer.pkl"
ENCODER_MODEL = "encoder.pkl"

# SENTIMENT
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)

# KERAS
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
SEQUENCE_LENGTH = 300

#UTILITY
import time
import pickle

# nltk
import nltk

# Downloading the necessary for preprocessing
nltk.download('stopwords')

def nlp():
    '''This function calls the scraper function which scrapes the past three days of tweets containing the selected company name.
    It performs a sentiment analysis of each tweet and gives the average over those three days.
    INPUT: NONE
    OUTPUT: sentiment average over the past three days.'''

    # Loads the saved keras model
    def load_models():

        # Load the tokenizer.
        file = open(path + TOKENIZER_MODEL, 'rb')
        tokenizer = pickle.load(file)
        file.close()
        # Load the model
        model = load_model(path + KERAS_MODEL)
        # Check its architecture
        model.summary()

        return tokenizer, model

    # Predicts the sentiment value for a tweet
    def predict(text, include_neutral=True):

        start_at = time.time()
        # Tokenize text
        x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
        # Predict
        score = model.predict([x_test])[0]
        # Decode sentiment
        #label = decode_sentiment(score, include_neutral=include_neutral)

        return float(score)


    # Loading the models.
    tokenizer, model = load_models()

    # Getting the texts
    all_text = scrape()

    # Preprocessing data
    all_text.text = all_text.text.apply(lambda x: preprocess(x))

    # Calculating the sum of scores from all tweets over the past three days
    score = 0
    for text in all_text.text:
      score = score + predict(text)

    # Calculating the average score for the sentiment over the past three days
    score = score/len(all_text)

    return(score)
