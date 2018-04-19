from flask import render_template
from flask import request

import time
import flask
from flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def index():
  print("potato")

  qs=request.query_string

  if qs:
    try:
      agent = request.headers.get('User-Agent')
      user_agent = {'User-agent': agent}
      rt = requests.get(qs.decode('utf8'), headers = user_agent).text
    except:
      rt = "nope"

    response = flask.Response(rt)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
  else:
    print("nope")

  return render_template('index.html')

