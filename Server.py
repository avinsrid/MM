#!/usr/bin/python

from flask import Flask, jsonify, render_template, request
from EchoNest import *
from Youtube import *
import requests
import random

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

    @app.route('/getPlayList/<environment>/<activity>', methods=["GET"])
    def GiveGenre(environment, activity):

        genre_list = {"blues":True, "jazz":True, "rock":True, "metal":True, "heavy metal":True, "r&b":True, "reggae":True, "hiphop":True, "dance":True, "electro":True, "pop":True, "house":True}
        environment_list = {"Library":True, "Room":True, "Car":True}
        action_list = {"Studying":True, "Sleeping":True, "Driving":True}
        genre_mood = {"Library-Studying": ["blues", "jazz", "reggae"], "Room-Sleeping": ["jazz", "blues", "rock"], "Car-Driving": ["dance", "hiphop", "house"]}

        if environment in environment_list:
            # user_mood = request.form["environment"] + '-' + request.form["activity"];
            user_mood = environment + '-' + activity;
            genre = random.choice(genre_mood[user_mood]);
            echoNest = EchoNest();
            data_json = echoNest.get_playlist(genre);
            return jsonify(data_json);
        else:
            return "error"
