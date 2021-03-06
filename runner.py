import os
import argparse
import json
import configparser
from Models.SpotLogger import SpotLogger
from Models.ScribeLogger import ScribeLogger
from Models.LiteLogger import LiteLogger

# set up arg parser
parser = argparse.ArgumentParser(description='Log Spotify data...')
# set up db-commit argument
parser.add_argument('-c', '--db-commit', type=int, help='1 to commit, 0 to not', default=0)

# Process cmd line args
args = parser.parse_args()

# set up config parser
config = configparser.ConfigParser()
config.read('config.txt')

# Spotify API Connect details
SPOTIPY_CLIENT_ID = config['SPOTIFY']['ClientID']
SPOTIPY_CLIENT_SECRET = config['SPOTIFY']['ClientSecret']
SPOTIPY_REDIRECT_URI = config['SPOTIFY']['RedirectURI']
SPOTIPY_USERNAME = config['SPOTIFY']['Username']
SPOTIPY_SCOPE = config['SPOTIFY']['Scope']

# JSON Output file
JSON_output_file = config['OUTPUTS']['json_output']

# sqlite variables
SPOTLOGGER_DB = config['OUTPUTS']['spotlogger_db']
# COMMIT_CONFIRM = int(config['OUTPUTS']['commit_confirm'])
COMMIT_CONFIRM = int(args.db_commit)

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

    # Connect to sqlitedb
    LiteLoggerOne.setup()

    # insert payload record(s)
    LiteLoggerOne.record_payload_sqllite(ScribeLoggerOne.payload_data)

    # commit SQLite Records if 1
    LiteLoggerOne.teardown(commit_confirm=COMMIT_CONFIRM)

    # insert context record(s)
    # LiteLoggerOne.record_context_sqllite(context_data)
    # LiteLoggerOne.record_track_sqllite(track_data)

    # insert artist record(s)
    # LiteLoggerOne.record_artist_sqllite(artist_data)

    # insert album record(s)
    # LiteLoggerOne.record_album_sqllite(album_data)

    # if 1 == 1:
    #    LiteLoggerOne.teardown(COMMIT_CONFIRM)
    # else:
    #    0
