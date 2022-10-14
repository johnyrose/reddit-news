import json

with open('config.json') as config_file:
    config = json.load(config_file)


REDDIT_USER = config['reddit']['user']
REDDIT_PASSWORD = config['reddit']['password']
REDDIT_CLIENT_ID = config['reddit']['clientId']
REDDIT_CLIENT_SECRET = config['reddit']['clientSecret']
REDDIT_USER_AGENT = config['reddit']['userAgent']

EXTRACTOR_API_TOKEN = config['extractor']['api_token']
EXTRACTOR_URL = config['extractor']['url']

SUBREDDITS_CONFIG = config['subreddits']
DB_FILE = config['db_file']
