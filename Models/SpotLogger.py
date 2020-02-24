import spotipy
import json
import _sqlite3


class SpotLogger:
    def __init__(self, username, scope, client_id, client_secret, redirect_uri, auth_method=0):
        self.username = username
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.auth_method = auth_method
        self.client = None  # will hold spotify client object
        self.recently_played_list = None # will hold returned 'recently played songs' json

    def get_spotify_auth_token(self):
        """Prompt for User Token
    get auth token
    else error
    """
        token = spotipy.util.prompt_for_user_token(
            self.username
            , self.scope
            , self.client_id
            , self.client_secret
            , self.redirect_uri
            , self.auth_method
        )

        if token:
            self.client = spotipy.Spotify(auth=token)
        else:
            print("Can't get token for", self.username)

    def get_recently_played_songs(self):
        """Prompt Spotify for JSON
    Fills self.recently_played_list with returned JSON
    current_user_recently_played() returns 50 songs max
    """
        self.recently_played_list = self.client.current_user_recently_played()

        if self.recently_played_list['next'] == '':
            print('all done')

        # need logic to deal with API return pagination

    def output_recently_played_to_json_file(self, dump_file):
        """use json.dump to output JSON
    """
        with open(dump_file, 'w') as list_file:
            json.dump(self.recently_played_list, list_file)
