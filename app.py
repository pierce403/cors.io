from flask import render_template
from flask import request

import time
import flask
from flask import Flask
app = Flask(__name__)

import requests

@app.route('/', methods=("GET", "POST", "OPTIONS"))
def index():
  qs=request.query_string

  if qs:
    try:
      qs = qs.decode('utf8')

      agent = request.headers.get('User-Agent')
      ctype = request.headers.get('Content-Type')

      user_agent = {'User-agent': agent}

      if request.method == "POST":
        user_data = {}
          
        if 'application/json' in ctype:
          user_data = request.data
        else:
          user_data = request.form.to_dict()

        if 'multipart/form-data' in ctype:
          user_files = request.files.to_dict()

          r = requests.post(qs, headers = user_agent, data = user_data, files = user_files)
        else:
          r = requests.post(qs, headers = user_agent, data = user_data)
      elif request.method == "GET":
        r = requests.get(qs, headers = user_agent)
      elif request.method == "OPTIONS":
        '''
        OPTIONS has recently been used before POST in some libraries
        but not all websites have an OPTIONS http method; therefore,
        we provide a request to ourself in order to return
        the correct headers with correct response code and data
        '''
        r = requests.options(request.base_url, headers = user_agent)

      rt = r.text
    except:
      return "nope"

    response = flask.Response(rt)
    status_code = r.status_code

    '''
    we don't really care if the requests.options above 
    returns an OK request or not, we just care about
    passing a new response with new headers, and a valid status code
    '''
    if request.method == "OPTIONS":
      status_code = 200

    response.headers['Access-Control-Allow-Origin'] = '*'

    '''
    preflight CORS policy response headers
      - Returns Allowed Methods:
          In our case, GET and POST are the only ones allowed
      - Returns Allowed Headers:
          In our case, it is the headers that the user requested to use
          so, the ones in Access-Control-Request-Headers
    '''
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = request.headers.get('Access-Control-Request-Headers')

    return response, status_code
  else:
    print("nope")

  return render_template('index.html')

