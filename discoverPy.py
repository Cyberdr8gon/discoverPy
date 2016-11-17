#!/usr/bin/env python3
import pprint
import sys

import spotipy
import spotipy.util as util


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print ("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name'])) 

def generatePlaylist(sHandle):
	
    # not actual code right now
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print
            print (playlist['name'])
            print ('  total tracks', playlist['tracks']['total'])
            results = sp.user_playlist(username, playlist['id'],
                fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks) 
    return

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username " % (sys.argv[0]))
    sys.exit()

scope = 'playlist-modify-public user-top-read user-library-read user-follow-read playlist-read-private'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    generatePlaylist(sp)
else:
    print ("Can't get token for", username)
