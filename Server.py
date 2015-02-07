#!/usr/bin/python

from flask import Flask, jsonify, render_template, request
import requests

class Server:

    app = Flask(__name__);
    CONST_PORT = 5000;
    CONST_HOST = '0.0.0.0';

    def __init__(self):
      self.app.config['DEBUG'] = True # Disable me in Deployment

    @app.route('/')
    def hello():
    	return render_template('hello.html');

    @app.route('/search', methods=["GET", "POST"])
    def search():
    	if request.method == "POST":
    		url="http://developer.echonest.com/api/v4/song/search?api_key=JFORRE0YYTK6BRWG9&format=json&style=" + request.form["user_search"] + \
    		"&results=99&sort=song_hotttnesss-desc";

    		return render_template('results.html', api_data=requests.get(url).json());
    		#return jsonify(requests.get(url).json());
    	else:
    		return  render_template('search.html');

    @app.errorhandler(404)
    def not_found(error):
    	return "Sorry, I haven't coded that yet, I'll get back to you...!!!", 404

    def run(self, hostID=None, portNo=None):
        if hostID is None:
            hostID=self.CONST_HOST;

        if portNo is None:
            portNo=self.CONST_PORT;
        self.app.run(host=hostID, port=portNo);
