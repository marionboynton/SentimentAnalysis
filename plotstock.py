from nlp import nlp
from preprocessing import preprocess
from scraper import scrape
import plotly
import plotly.express as px
import plotly.graph_objs as go
import json
import get_db_data

sentiment = nlp()
df_stocks = get_db_data.get_stock_prices(sentiment)
df_sent = get_db_data.get_14_day_sentiment(sentiment)


def plotgraph(dfstocks=df_stocks):
    data = [go.Scatter(x=dfstocks["Date"], y=dfstocks["Close"])]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    #fig = px.line(dfstocks,x="Date", y="Close")
    return graphJSON

def plotsent(df_sent=df_sent):
    datasent = [go.Scatter(x=df_sent["index"], y=df_sent["sentiment"])]
    graphsentJSON = json.dumps(datasent, cls=plotly.utils.PlotlyJSONEncoder)
    #fig = px.line(dfstocks,x="Date", y="Close")
    return graphsentJSON
