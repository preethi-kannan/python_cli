import requests
import json

# Searches and returns top track name based on lyrics using Musixmatch API

def getSong(search):

	base_url = "https://api.musixmatch.com/ws/1.1/tracksearch?format=json&callback=callback&q_lyrics="
	song_base = formatLyrics(search)

	api_call = "https://api.musixmatch.com/ws/1.1/track.search?format=json&callback=callback&q_lyrics=" + song_base + "&s_track_rating=desc&quorum_factor=1&apikey=d13209ab1b8ab754435bcfc4301e696a"
	
	request = requests.get(api_call)
	data = request.json()
	data = data['message']['body']
	
	if data['track_list']:
		data = data['track_list'][0]['track']['track_name']

	else:
		print("Sorry I couldn't find any songs with those lyrics")

	return data


def formatLyrics(search):
	base = "%22"
	lyric_split = search.split()
	for i in range(len(lyric_split)):
		base = base + lyric_split[i] + "%20"

	base = base[:-1]
	base = base + "2"
	return base
