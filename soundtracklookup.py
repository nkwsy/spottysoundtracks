import time
import spotify

from imdb import IMDb


####
import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util
########


ia = IMDb()
s_result = ia.search_movie('The Untouchables')
print s_result[0]


ts = ia.get_movie('0113247')
ia.update(ts, 'soundtrack')
tracks = ts['soundtrack']
print tracks[3]





# Creates a playlist for a users

util.prompt_for_user_token()
sp = spotipy.Spotify(auth=token)
sp.trace = False
playlists = sp.user_playlist_create(username, playlist_name)
pprint.pprint(playlists)





# if len(sys.argv) > 2:
#     username = sys.argv[1]
#     playlist_name = sys.argv[2]
# else:
#     print("Usage: %s username playlist-name" % (sys.argv[0],))
#     sys.exit()

# token = util.prompt_for_user_token(username)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     sp.trace = False
#     playlists = sp.user_playlist_create(username, playlist_name)
#     pprint.pprint(playlists)
# else:
# 	print("Can't get token for", username)



