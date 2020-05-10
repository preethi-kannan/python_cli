import sys 
import spotipy
import spotipy.util as util


# Finds all playlists owned by user and then determines 
# if the playlist input is an existing playlist

def getPlaylist(playlist_name, song_name, username):

	scope = 'playlist-read-private'
	token = util.prompt_for_user_token(username,
		scope,
		"c191fdd1e95f4383aafa976bf4ec761a",
		"3d39f727fb764ea79a715bdff69e0d54",
		"http://127.0.0.1:9090")

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
					
	else:
		print("can't get token for", username)

	if playlistfound:
		print("The playlist was found")
		print()
	else:
		print("Uh oh couldn't find that playlist")
		print()

	return playlist_id, playlistfound


# Adds found song into desired playlist if not already
# found in playlist

def addToPlaylist(playlist_id, track_id, username):

	scope = 'playlist-modify-public'
	token = util.prompt_for_user_token(username,
		scope, 
		"c191fdd1e95f4383aafa976bf4ec761a",
		"3d39f727fb764ea79a715bdff69e0d54",
		"http://127.0.0.1:9090")

	if token:
		sp = spotipy.Spotify(auth = token)
		sp.trace = False
		duplicateExists = checkIfSongExistsinPlaylist(playlist_id, track_id, username)
		if (not duplicateExists):
			results  = sp.user_playlist_add_tracks(username, playlist_id, [track_id])
			print()
			print("Bust down Thotiana!")
		
	else: 
		print("can't get token")

# Checks if song is already in playlist

def checkIfSongExistsinPlaylist(playlist_id, track_id, username):

	scope = 'playlist-modify-public'
	token = util.prompt_for_user_token(username,
		scope, 
		"c191fdd1e95f4383aafa976bf4ec761a",
		"3d39f727fb764ea79a715bdff69e0d54",
		"http://127.0.0.1:9090")

	if token:
		sp = spotipy.Spotify(auth = token)
		sp.trace = False
		results = sp.user_playlist_tracks(username, playlist_id)
		tracks = results['items']
		for track in tracks: 
			if track['track']['id'] == track_id:
				print("That track already exists in this playlist!")
				print()
				return True

	return False


#Creates new playlist if playlist does not exist

def createNewPlaylist(playlist_name, username):

	scope = 'playlist-modify-public'
	token = util.prompt_for_user_token(username,
		scope, 
		"c191fdd1e95f4383aafa976bf4ec761a",
		"3d39f727fb764ea79a715bdff69e0d54",
		"http://127.0.0.1:9090")

	new_id = ""

	if token:
		sp = spotipy.Spotify(auth = token)
		result = sp.user_playlist_create(username, playlist_name)
		new_id = result['id']
		
	else: 
		print("Can't get token")

	return new_id




