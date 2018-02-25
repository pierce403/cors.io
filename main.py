import webapp2
from time import time
from google.appengine.api import urlfetch
import urllib2

class MainPage(webapp2.RequestHandler):
  def get(self):

    if self.request.query_string:
      self.response.headers.add_header("Access-Control-Allow-Origin", "*")
      hdr = { 'User-Agent' : self.request.headers['User-Agent'] }
      req = urllib2.Request(self.request.query_string, headers=hdr)
      self.response.out.write(urllib2.urlopen(req).read())

    else:
      self.response.out.write('''
<html><head><title>cors.io</title></head>
<body><center><br><br>

<big><b>The Problem:</b></big><br>
No 'Access-Control-Allow-Origin' header is present on the requested resource.
<br>Origin 'http://internet.derp' is therefore not allowed access.<br><br>

<big><b>The Solution:</b></big><br>
A CORS proxy!<br><br>


$.getJSON('https://blockchain.info/stats?format=json',function(){})<br><br>

becomes ..<br><br>

$.getJSON('<b>https://cors.io/?</b>https://blockchain.info/stats?format=json',function(){})<br><br>

send hatemail to <a href="https://twitter.com/deanpierce">@deanpierce</a>

''')

  def post(self):

    if self.request.query_string:
      self.response.headers.add_header("Access-Control-Allow-Origin", "*")
      hdr = { 'User-Agent' : self.request.headers['User-Agent'] }
      req = urllib2.Request(self.request.query_string, self.request.arguments(), headers=hdr)
      res = urllib2.urlopen(req)
      self.response.headers['Content-Type'] = res.info().type
      self.response.out.write(res.read())

app = webapp2.WSGIApplication([('/',MainPage)])
