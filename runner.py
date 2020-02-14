import os
from Models.SpotLogger import SpotLogger
from Models.LiteLogger import LiteLogger

# Spotify API Connect details
SPOTIPY_CLIENT_ID = None
SPOTIPY_CLIENT_SECRET = None
SPOTIPY_REDIRECT_URI = 'http://google.com'
SPOTIPY_USERNAME = 'penroff4@gmail.com'
SPOTIPY_SCOPE = 'user-read-recently-played'

# sqlite variables
SPOTLOGGER_DB = os.getcwd()+"\data\SpotLogger.db"
COMMIT_CONFIRM = None

# Create SpotLogger to call Spotify
SpotLoggerOne = SpotLogger.SpotLogger(
    SPOTIPY_USERNAME
    , SPOTIPY_SCOPE
    , SPOTIPY_CLIENT_ID
    , SPOTIPY_CLIENT_SECRET
    , SPOTIPY_REDIRECT_URI
)

# Create LiteLogger to log results to sqlite
LiteLoggerOne = LiteLogger.LiteLogger(
    SPOTLOGGER_DB
)

###_MAIN_###

#  prompts user to authorize app
SpotLoggerOne.get_spotify_auth_token()

#  gets json of recently played tracks from spotify
SpotLoggerOne.get_recently_played_songs()

#  outputs json to file
SpotLoggerOne.output_recently_played_to_json_file()

# operate over JSON to build payload table
# payload_data = []

# operate over JSON to build context table
# context_data = []

# operate over JSON to build track table
# track_data = []

# operate over JSON to build artist table
# artist_data = []

# operate over JSON to build album table
# album_data = []

# Connect to sqlitedb
LiteLoggerOne.setup()

# insert payload record(s)
LiteLoggerOne.record_payload_sqllite(payload_data)

# insert context record(s)
LiteLoggerOne.record_context_sqllite(context_data)

# insert track record(s)
LiteLoggerOne.record_track_sqllite(track_data)

# insert artist record(s)
LiteLoggerOne.record_artist_sqllite(artist_data)

# insert album record(s)
LiteLoggerOne.record_album_sqllite(album_data)

if true:
    LiteLoggerOne.teardown(COMMIT_CONFIRM)
else:
    return false

