from flask import Flask, render_template
from nlp import nlp
import plotstock

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/viz')
def plot_wrap():
    show=plotstock.plotgraph()
    sent = nlp()
    showsent=plotstock.plotsent()
    return render_template('plot.html',show=show, sent=sent, showsent=showsent)


if __name__=="__main__":
     app.run(debug=True)
