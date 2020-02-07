"""
# mac OS
import os
os.system('')
"""

"""
Left over from initial Windows environ variable set
# res = subprocess.check_output('set-CLI.bat')
#subprocess.check_output('echo %SPOTIPY_REDIRECT_URI%')
"""
import subprocess

"""
  set 
    SPOTIPY_CLIENT_ID
    SPOTIPY_CLIENT_SECRET
    SPOTIPY_REDIRECT_URI
"""

subprocess.run('set-CLI.bat')

util.prompt_for_user_token(
      'username'
    , 'scope'
    , os.environ['%SPOTIPY_CLIENT_ID']
    , os.environ['SPOTIPY_CLIENT_SECRET']
    , os.environ['SPOTIPY_CLIENT_']
)