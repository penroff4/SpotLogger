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

    # build self.payload_data
    ScribeLoggerOne.prep_payload_data()

    # build items_df
    ScribeLoggerOne.prep_items_df()

    # build tracks df
    ScribeLoggerOne.prep_tracks_df(ScribeLoggerOne.items_df)

    # 'fix' artist_holder object, ie flatten out the external urls section
    ScribeLoggerOne.artist_holder = ScribeLoggerOne.flatten_artist_holder(ScribeLoggerOne.artist_holder)

    # build artist df
    ScribeLoggerOne.prep_artist_df(ScribeLoggerOne.artist_holder)

    # build album df
    ScribeLoggerOne.prep_album_df(ScribeLoggerOne.album_holder)

    # update tracks df

    # build context df

    # Connect to sqlitedb
    LiteLoggerOne.setup()

    # insert payload record(s)
    LiteLoggerOne.record_payload_sqllite(ScribeLoggerOne.payload_data)

    ###                         NOTE TO SELF                        ###
    ### I realize now that the dim tables (eg artist, album, track) ###
    ### will all need logic to check for existing records as well   ###
    ### as logic for updates.  i.e. I'll need to read in the        ###
    ### existing SQL table, turn that into a DF to work over, and   ###
    ### then comapre.  Womp womp                                    ###

    # update artist data
    # LiteLoggerOne.record_artist_sqllite(ScribeLoggerOne.artist_data)

    # update album record(s)
    # LiteLoggerOne.record_album_sqllite(album_data)

    # update track table

    # record context data

    # insert context record(s)
    # LiteLoggerOne.record_context_sqllite(context_data)
    # LiteLoggerOne.record_track_sqllite(track_data)

    # commit SQLite Records if 1
    LiteLoggerOne.teardown(commit_confirm=COMMIT_CONFIRM)

