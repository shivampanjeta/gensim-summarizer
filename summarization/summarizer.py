import json
import flask
from gensim.summarization.summarizer import summarize

# The flask app for serving predictions
app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return flask.Response(response='\n', status=200, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def summarize():
    data = request.data
    summary = summarize(data)
    return flask.Response(response=summary, status=200)
