#Performs all the necessary preprocessing and cleaning for the tweet sentiment analysis
def preprocess(text, stem=False):

    # Define the stopwords and stemmer
    stop_words = stopwords.words("english")
    stemmer = SnowballStemmer("english")

    # Remove link,user and special characters
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
    
    tokens = []
    for token in text.split():
      if token not in stop_words:
          if stem:
              tokens.append(stemmer.stem(token))
          else:
              tokens.append(token)
    return " ".join(tokens)