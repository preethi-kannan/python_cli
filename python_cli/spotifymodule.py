import requests, json, spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

def getTrack(song_name):
	

	cid = "c191fdd1e95f4383aafa976bf4ec761a"
	csecret = "3d39f727fb764ea79a715bdff69e0d54"

	client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=csecret)
	sp = spotipy.Spotify(client_credentials_manager
	= client_credentials_manager)


	track_results = sp.search(q=song_name, type='track', limit=1, offset=0)
	for i, t in enumerate(track_results['tracks']['items']):
		artist = t['artists'][0]['name']
		track_name = t['name']
		album_name = t['album']['name']
		popularity = t['popularity']
		track_id = t['id']

	print("This track is called: " + track_name)
	print("This track is by: " + artist)
	print("This track shows up on: " + album_name)
	print("This track is " + str(popularity) + " points popular")
	
	return track_id

	
