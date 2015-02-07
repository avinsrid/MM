#!/usr/bin/python

from flask import Flask, jsonify, render_template, request
from EchoNest import *
from Youtube import *
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
            echoNest = EchoNest(); #I hate Python
            data_json = echoNest.get_playlist(request.form["user_search"]);
            return render_template('results.html', api_data=data_json);
    	else:
    		return render_template('search.html');


    @app.route('/play_music', methods=["POST"])
    def play_music():
        youtube = Youtube();
        data_json = youtube.obtain_video_id(request.form["artist_name"], request.form["song_name"]);
        return render_template('youtube.html', api_data=data_json);

    @app.errorhandler(404)
    def not_found(error):
    	return "Sorry, I haven't coded that yet, I'll get back to you...!!!", 404

    def run(self, hostID=None, portNo=None):
        if hostID is None:
            hostID=self.CONST_HOST;

        if portNo is None:
            portNo=self.CONST_PORT;

        self.app.run(host=hostID, port=portNo);
