def preprocess(text, stem=False):
  '''This function does all the necessary preprocessing and cleaning of the texts
  so that they can be fed to the nlp for sentiment analysis.
  INPUT: a text (string)
  OUTPUT:  the cleaned text (string)'''

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