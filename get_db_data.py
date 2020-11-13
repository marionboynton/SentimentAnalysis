import pandas as pd
import mysql.connector as mysql

# Create connection string for query processing
conn = mysql.connect(
host = "localhost",
database = "datatwitter",
user = "root",
password = "password")

def get_closest_date(nlp_sentiment):

    q = """(SELECT
                datatwitter.sentiment_data.index as DateOfInterest,sentiment,
                ABS(sentiment - {input_sentiment}) as distance
            FROM datatwitter.sentiment_data)
            ORDER BY
                ABS(sentiment - {input_sentiment}) ASC
            LIMIT 1;""".format(input_sentiment = nlp_sentiment)

    date = pd.read_sql(q, conn).iloc[0,0].date()
    return date



def get_stock_prices (nlp_sentiment):
    closest_date = get_closest_date(nlp_sentiment)

    query = """
    SELECT *
    FROM datatwitter.stock_prices
    WHERE datatwitter.stock_prices.date >= '{date}'
    ORDER BY datatwitter.stock_prices.date ASC
    LIMIT 14
    ;""".format(date = closest_date)

    df = pd.read_sql(query, conn)

    return df

def get_14_day_sentiment(nlp_sentiment):

    closest_date = get_closest_date(nlp_sentiment)

    query = """
    SELECT *
    FROM datatwitter.sentiment_data
    WHERE datatwitter.sentiment_data.index >= '{date}'
    ORDER BY datatwitter.sentiment_data.index ASC
    LIMIT 14
    ;""".format(date = closest_date)

    df = pd.read_sql(query, conn)

    return df
