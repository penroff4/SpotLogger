import os

# for i in os.environ:
#   print(i)

spotipy_var = ['SPOTIPY_CLIENT_ID', 'SPOTIPY_CLIENT_SECRET', 'SPOTIPY_REDIRECT_URI']

for i in spotipy_var:
    print(os.environ[i])
