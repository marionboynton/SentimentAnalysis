from flask import Flask, render_template
from nlp import nlp
import plotstock

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/vizy')
def plot_wrap():
    graph=plotstock.plotgraph()
    return render_template('plot.html',graph=graph)

# if __name__=="__main__":
#     app.run(debug=True)
