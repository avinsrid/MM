#!/usr/bin/python

import json
import requests

class Youtube:

	base_url = "https://www.googleapis.com/youtube/v3/search?part=id&q="
	auth_key = "&key=AIzaSyAeKbab6aWGaO1u2L1UyTpJjTqVZSzA7pE"

	def obtain_video_id(self, artist_name, song_name):
		final_url = self.base_url + artist_name + "-" + song_name + self.auth_key
		response = requests.get(final_url)
		output = response.json()
		video_id = output["items"][0]["id"]["videoId"]
		return video_id
