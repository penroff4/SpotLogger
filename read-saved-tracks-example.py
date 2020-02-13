import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = 'penroff4@gmail.com'

SPOTIPY_CLIENT_ID = '790fb465c980470886e0887c7c02cb7a'
SPOTIPY_CLIENT_SECRET = 'a41fec8061c54bfd94c1d857c2965ba5'
# SPOTIPY_REDIRECT_URI = 'http://localhost/8080/callback/'
SPOTIPY_REDIRECT_URI = 'http://google.com'

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)


