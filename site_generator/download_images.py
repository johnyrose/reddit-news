import os
import requests

from common.logger import logger
from common.settings import LOCAL_IMAGES_FOLDER
from models.website.website import Website, WebsiteArticle


def download_image_from_url(url: str, filename: str):
    img_data = requests.get(url).content
    with open(filename, 'wb') as handler:
        handler.write(img_data)


def modify_article_to_use_local_images(article: WebsiteArticle):
    filename = f'{LOCAL_IMAGES_FOLDER}/{article.id}.jpg'
    download_image_from_url(article.image_url, filename)
    article.image_url = filename


def download_images_locally(website: Website):
    logger.info('Downloading images locally...')
    if not os.path.exists(LOCAL_IMAGES_FOLDER):
        os.makedirs(LOCAL_IMAGES_FOLDER)
    modify_article_to_use_local_images(website.main_article)
    for article in website.sub_articles:
        modify_article_to_use_local_images(article)
    for article in website.mini_articles:
        modify_article_to_use_local_images(article)
    for news_row in website.news_rows:
        for article in news_row.articles:
            modify_article_to_use_local_images(article)
