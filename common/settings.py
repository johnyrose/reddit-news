import json
import os
from models.website.sorting_method import SortingMethod


CONFIG_FILE = os.getenv('CONFIG_FILE', 'config.json')
with open(CONFIG_FILE) as config_file:
    config = json.load(config_file)

PERFORM_DATA_COLLECTION = config['tasks_to_perform']['data_collection']
PERFORM_WEBSITE_GENERATION = config['tasks_to_perform']['website_generation']

REDDIT_USER = config['external_apis']['reddit']['user']
REDDIT_PASSWORD = config['external_apis']['reddit']['password']
REDDIT_CLIENT_ID = config['external_apis']['reddit']['clientId']
REDDIT_CLIENT_SECRET = config['external_apis']['reddit']['clientSecret']
REDDIT_USER_AGENT = config['external_apis']['reddit']['userAgent']

EXTRACTOR_API_TOKEN = config['external_apis']['extractor']['api_token']
EXTRACTOR_URL = config['external_apis']['extractor']['url']

URLMETA_URL = config['external_apis']['urlmeta']['url']
URLMETA_EMAIL = config['external_apis']['urlmeta']['email']
URLMETA_API_TOKEN = config['external_apis']['urlmeta']['api_token']

SUBREDDITS_CONFIG = config['subreddits']

DB_FILE = config["general_settings"]['db_file']
ENABLE_SQLALCHEMY_LOGGING = config["general_settings"]['enable_sqlalchemy_logging']
MAX_PARALLEL_REQUESTS = config["general_settings"]['max_parallel_requests']
TEMPLATE_FILE = config["general_settings"]['template_file']
OUTPUT_FILE = config["general_settings"]['output_file']
LOCAL_IMAGES_FOLDER = config["general_settings"]['local_images_folder']
USE_LOCAL_IMAGES = config["general_settings"]['use_local_images']

MAIN_ARTICLES_MAX_LENGTH = config['website']['text_length']['main_article']
SUB_ARTICLES_MAX_LENGTH = config['website']['text_length']['sub_articles']
MINI_ARTICLES_MAX_LENGTH = config['website']['text_length']['mini_articles']
NEWS_ROW_MAX_LENGTH = config['website']['text_length']['news_rows_articles']

SUB_ARTICLES_AMOUNT = config['website']['articles_amount']['sub_articles']
MINI_ARTICLES_AMOUNT = config['website']['articles_amount']['mini_articles']
NEWS_ROW_ARTICLE_AMOUNT = config['website']['articles_amount']['news_row_articles']

TITLES_MAX_LENGTH = config['website']['text_length']['titles']

MINIMUM_ARTICLES_AMOUNT_WARNING = 1 + SUB_ARTICLES_AMOUNT + MINI_ARTICLES_AMOUNT + NEWS_ROW_ARTICLE_AMOUNT

try:
    SORTING_METHOD = SortingMethod(config['website']['sorting_method'])
except ValueError:
    raise ValueError(f'Invalid sorting method: {config["website"]["sorting_method"]}. '
                     f'Valid values: {list(SortingMethod.__members__.keys())}')
