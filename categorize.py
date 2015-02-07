import json
import httlib2
import random

genre_list = {"blues":True, "jazz":True, "rock":True, "metal":True, "heavy metal":True, "r&b":True, "reggae":True, "hiphop":True, "dance":True, "electro":True, "pop":True, "house":True}
environment_list = {"Library":True, "Room":True, "Car":True}
action_list = {"Studying":True, "Sleeping":True, "Driving":True}
genre_mood = {"Library-Studying": ["blues", "jazz", "reggae"], "Room-Sleeping": ["jazz", "blues", "rock"], "Car-Driving": ["dance", "hiphop", "house"]}

def GiveGenre(user_environment, user_action, hotness):
	if hotness is True:
		return "hotttnesss"
	else:
		if user_environment in environment_list:
			user_mood = user_environment + user_action
			genre = random.(genre_mood[user_mood])
			return genre
		else:
			return "error"


