import requests

from common.settings import EXTRACTOR_URL, EXTRACTOR_API_TOKEN


def get_text_from_article_url(article_url: str):
    res = requests.get(f'{EXTRACTOR_URL}/?apikey={EXTRACTOR_API_TOKEN}&{article_url}')


def generate_articles():
    current_posts =