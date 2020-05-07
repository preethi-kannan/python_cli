import sys 
import spotipy
import spotipy.util as util

from .playlistmodule import getPlaylist, addToPlaylist, createNewPlaylist
from .spotifymodule import getTrack
from .searchmodule import *


def main():

    arg = sys.argv[1]

    original_search = arg
    print("Is this\n1. Lyrics\n2. Song Title")
    input_type = input(">")


    if (input_type == "1"):
        lyric_search = getSong(arg)
        print(lyric_search)
        track_id = getTrack(lyric_search)
    else:
        track_id = getTrack(original_search)


    g = input("Add to playlist? (Y/N) ")
    if (g != "Y"):
    	return

    playlist_name = input("Which playlist? ")
    username = input("Username: ")

    playlist_id = getPlaylist(playlist_name, "sdfjfnsdkf", username)

    if playlist_id[1] == True:
        addToPlaylist(playlist_id[0], track_id, username)
        print()
        print("Bust down thotiana!")
    else:
        print()
        print("Creating new playlist...")
        new_id = createNewPlaylist(playlist_name, username)
        addToPlaylist(new_id, track_id, username)
        # print()


   

if __name__ == '__main__':
    main()