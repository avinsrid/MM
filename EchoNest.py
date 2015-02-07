#!/usr/bin/python

from flask import jsonify
import requests

class EchoNest:

    base_url = "http://developer.echonest.com/api/v4/song/search?";
    auth_key = "&api_key=JFORRE0YYTK6BRWG9";

    def get_playlist(self, user_search):

      url= self.base_url + "format=json&style=" + user_search + "&results=99&sort=song_hotttnesss-desc" + self.auth_key;
      return requests.get(url).json();
