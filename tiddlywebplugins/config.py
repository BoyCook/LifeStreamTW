import os

config = {
    'app_key': os.environ['APP_KEY'],    
    'app_secret': os.environ['APP_SECRET'],
    'oauth_token': os.environ['OAUTH_TOKEN'],
    'oauth_token_secret': os.environ['OAUTH_TOKEN_SECRET']
}
