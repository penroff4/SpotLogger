echo off

Rem set global variables
set SPOTIPY_CLIENT_ID='790fb465c980470886e0887c7c02cb7a'
set SPOTIPY_CLIENT_SECRET='a41fec8061c54bfd94c1d857c2965ba5'
Rem set SPOTIPY_REDIRECT_URI='http://localhost/8888/callback/'

set SPOTIPY_REDIRECT_URI='http://google.com'

Rem User imput for SpotLogger Object variables
Rem set /p SPOTIPY_USERNAME='Username: '
Rem set /p SPOTIPY_SCOPE='Scope: '

Rem Optional global variables in case not using user input
set SPOTIPY_USERNAME='penroff4@gmail.com'
set SPOTIPY_SCOPE='user-read-recently-played'

echo on