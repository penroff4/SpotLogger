import os
import json
from Models.SpotLogger import SpotLogger
from Models.ScribeLogger import ScribeLogger
from Models.LiteLogger import LiteLogger

# Spotify API Connect details
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = 'http://google.com'
SPOTIPY_USERNAME = ''
SPOTIPY_SCOPE = 'user-read-recently-played'

# JSON Output file
JSON_output_file = 'recently-played-list.txt'

# sqlite variables
SPOTLOGGER_DB = os.getcwd()+"\data\SpotLogger.db"
COMMIT_CONFIRM = None

# Create SpotLogger to call Spotify
SpotLoggerOne = SpotLogger(
    SPOTIPY_USERNAME
    , SPOTIPY_SCOPE
    , SPOTIPY_CLIENT_ID
    , SPOTIPY_CLIENT_SECRET
    , SPOTIPY_REDIRECT_URI
)

# Create ScribeLogger to prep data into records
ScribeLoggerOne = ScribeLogger(
    JSON_output_file
)

# Create LiteLogger to log results to sqlite
LiteLoggerOne = LiteLogger(
    SPOTLOGGER_DB
)

if __name__ == "__main__":

    #  prompts user to authorize app
    SpotLoggerOne.get_spotify_auth_token()

    #  gets json of recently played tracks from spotify
    SpotLoggerOne.get_recently_played_songs()

    #  takes dump_file, outputs JSON to dump_file
    SpotLoggerOne.output_recently_played_to_json_file(JSON_output_file)

    # read dump_file back in as JSON, self.rpl_json
    ScribeLoggerOne.read_json()
    
    # build payload_df
    ScribeLoggerOne.prep_payload_data()

    # build self.payload_data
    ScribeLoggerOne.prep_payload_data()

    # build items_df
    ScribeLoggerOne.prep_items_df()

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
    # LiteLoggerOne.setup()

    # insert payload record(s)
    # LiteLoggerOne.record_payload_sqllite(payload_data)

    # insert context record(s)
    # LiteLoggerOne.record_context_sqllite(context_data)

    # insert track record(s)
    # LiteLoggerOne.record_track_sqllite(track_data)

    # insert artist record(s)
    # LiteLoggerOne.record_artist_sqllite(artist_data)

    # insert album record(s)
    # LiteLoggerOne.record_album_sqllite(album_data)

    # if 1 == 1:
    #    LiteLoggerOne.teardown(COMMIT_CONFIRM)
    # else:
    #    0
