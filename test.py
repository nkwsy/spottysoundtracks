import pprint
import sys

import spotipy
import spotipy.util as util
from settings import SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, SPOTIPY_CLIENT_ID

username = 'nickjwesley'
scope = 'playlist-modify-public'

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

if len(sys.argv) > 3:
	    username = sys.argv[1]
	    playlist_id = sys.argv[2]
	    track_ids = sys.argv[3:]
else:
        print "Usage: %s username playlist_id track_id ..." % (sys.argv[0],)
	sys.exit()
if token:
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
	print results
else:
	print "Can't get token for", username


