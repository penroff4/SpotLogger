import spotipy
from pprint import pprint

AUTH_METHOD = 1  # Authorization Code if 0, Client Credentials if 1

SPOTIPY_CLIENT_ID = '790fb465c980470886e0887c7c02cb7a'
SPOTIPY_CLIENT_SECRET = 'a41fec8061c54bfd94c1d857c2965ba5'
SPOTIPY_REDIRECT_URI = 'http://localhost/8080/callback/'
SPOTIPY_USERNAME = 'penroff4@gmail.com'
SPOTIPY_SCOPE = 'user-read-recently-played'

token = spotipy.util.prompt_for_user_token(
    SPOTIPY_USERNAME
    , SPOTIPY_SCOPE
    , SPOTIPY_CLIENT_ID
    , SPOTIPY_CLIENT_SECRET
    , SPOTIPY_REDIRECT_URI
        )
