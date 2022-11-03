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

MAIN_ARTICLES_MAX_LENGTH = config['website']['text_length']['main_article']
SUB_ARTICLES_MAX_LENGTH = config['website']['text_length']['sub_articles']
MINI_ARTICLES_MAX_LENGTH = config['website']['text_length']['mini_articles']
NEWS_ROW_MAX_LENGTH = config['website']['text_length']['news_rows_articles']

SUB_ARTICLES_AMOUNT = config['website']['articles_amount']['sub_articles']
MINI_ARTICLES_AMOUNT = config['website']['articles_amount']['mini_articles']
NEWS_ROW_ARTICLE_AMOUNT = config['website']['articles_amount']['news_row_articles']

TITLES_MAX_LENGTH = config['website']['text_length']['titles']

MINIMUM_ARTICLES_AMOUNT_WARNING = 1 + SUB_ARTICLES_AMOUNT + MINI_ARTICLES_AMOUNT + NEWS_ROW_ARTICLE_AMOUNT
