# import subprocess
from Models.SpotLogger import SpotLogger

# subprocess.run('set-CLI.bat')
"""
    set the below system variables:pycharm 
        SPOTIPY_CLIENT_ID
        SPOTIPY_CLIENT_SECRET
        SPOTIPY_REDIRECT_URI
        SPOTIPY_USERNAME
        SPOTIPY_SCOPE
"""

SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = 'http://google.com'
SPOTIPY_USERNAME = 'penroff4@gmail.com'
SPOTIPY_SCOPE = 'user-read-recently-played'

SpotLoggerOne = SpotLogger.SpotLogger(
    SPOTIPY_USERNAME
    , SPOTIPY_SCOPE
    , SPOTIPY_CLIENT_ID
    , SPOTIPY_CLIENT_SECRET
    , SPOTIPY_REDIRECT_URI
)

#  prompts user to authorize app
SpotLoggerOne.get_spotify_auth_token()

#  gets json of recently played tracks from spotify
SpotLoggerOne.get_recently_played_songs()

#  outputs json to file
SpotLoggerOne.output_recently_played_to_json_file()

# record payload details

# record
