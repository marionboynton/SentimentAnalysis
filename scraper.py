# UPDATE: this is the selected company (query for the tweet search)
COMPANY = 'apple'

import tweepy
import datetime
import pandas as pd
import re

def scrape():
  '''This function scrapes twitter data which mentions the selected company.
  It gets the data for the past three days and returns a dataframe.
  INPUT: NONE
  OUTPUT: dataframe with text from twitter mentioning the selected company. One row per tweet. '''

  access_token = "1289900179701800960-2lujUQFC8RbuCcOgDMbloRzYPQY7ve"
  access_token_secret = "7hWUucfMm6oYutWWTBWdCu0RbIIJylfHOM6F0d8CtgH3e"
  consumer_key = "SJVSihso9VGRMpCC1acdbGk5M"
  consumer_secret = "TgQLnyhlEwQSIL9tsBVxwW7NNnxWhO5YaYhLN8brlH1WVjiw4x"


  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  
  #Dates for scraping tweets: from three days ago until today
  startDate=datetime.datetime.today()-datetime.timedelta(days=1)
  endDate=datetime.datetime.today()

  #Scrape the data
  text  =[]
  for tweet in tweepy.Cursor(api.search, q=COMPANY, lang="en").items(100):
      #keep only the past 3 days
      if tweet.created_at <= endDate and tweet.created_at >= startDate:
        text.append(tweet.text)

  #dump into a panda
  text_series = pd.Series(text)

  #Perform basica cleaning: remove @mentions, #hastags and URLs

  text_series = text_series.str.replace('@[A-Za-z0Ã¢â‚¬â€œ9]+', '', regex=True)
  text_series = text_series.str.replace('#', '', regex=True)
  text_series = text_series.str.replace('RT[\s]+', '', regex=True)

  #Return in the form of a dataframe
  text_df = pd.DataFrame({'text': text_series})
  
  return(text_df)