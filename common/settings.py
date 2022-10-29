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

MAX_PARALLEL_REQUESTS = config['max_parallel_requests']

URLMETA_URL = config['urlmeta']['url']
URLMETA_EMAIL = config['urlmeta']['email']
URLMETA_API_TOKEN = config['urlmeta']['api_token']

SUBREDDITS_CONFIG = config['subreddits']
DB_FILE = config['db_file']
ENABLE_SQLALCHEMY_LOGGING = config['enable_sqlalchemy_logging']

TEMPLATE_FILE = config['template_file']
OUTPUT_FILE = config['output_file']

MAIN_ARTICLES_MAX_LENGTH = config['website']['main_article_max_length']
SUB_ARTICLES_MAX_LENGTH = config['website']['sub_articles_max_length']
MINI_ARTICLES_MAX_LENGTH = config['website']['mini_articles_max_length']
NEWS_ROW_MAX_LENGTH = config['website']['news_row_max_length']

TITLES_MAX_LENGTH = config['website']['titles_max_length']
