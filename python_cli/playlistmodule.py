import sys 
import spotipy
import spotipy.util as util

def getPlaylist(playlist_name, song_name, username):

	scope = 'playlist-read-private'
	token = util.prompt_for_user_token(username,
		scope,
		"c191fdd1e95f4383aafa976bf4ec761a",
		"3d39f727fb764ea79a715bdff69e0d54",
		"https://localhost:8080")

	playlistfound = False
	playlist_id = ""

	if token:
		sp = spotipy.Spotify(auth=token)
		playlists = sp.user_playlists(username)

		for playlist in playlists['items']:
			if playlist['owner']['id'] == username:

				if playlist['name'] == playlist_name: 
					
					playlistfound = True
					playlist_id = playlist['id']
				print(playlist['name'])
					
	else:
		print("can't get token for", username)

	if playlistfound:
		print("The playlist was found")
	else:
		print("Uh oh couldn't find that playlist")

	return playlist_id, playlistfound


def addToPlaylist(playlist_id, track_id, username):

	scope = 'playlist-modify-public'
	token = util.prompt_for_user_token(username,
		scope, 
		"c191fdd1e95f4383aafa976bf4ec761a",
		"3d39f727fb764ea79a715bdff69e0d54",
		"https://localhost:8080")

	if token:
		sp = spotipy.Spotify(auth = token)
		sp.trace = False
		results  = sp.user_playlist_add_tracks(username, playlist_id, [track_id])
		
	else: 
		print("can't get token")


def createNewPlaylist(playlist_name, username):

	scope = 'playlist-modify-public'
	token = util.prompt_for_user_token(username,
		scope, 
		"c191fdd1e95f4383aafa976bf4ec761a",
		"3d39f727fb764ea79a715bdff69e0d54",
		"https://localhost:8080")

	new_id = ""

	if token:
		sp = spotipy.Spotify(auth = token)
		result = sp.user_playlist_create(username, playlist_name)
		new_id = result['id']
		
	else: 
		print("Can't get token")

	return new_id




