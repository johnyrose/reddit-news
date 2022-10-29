import base64

import requests

from common.db_connector import session_object
from multiprocessing.pool import ThreadPool
from common.settings import EXTRACTOR_URL, EXTRACTOR_API_TOKEN, URLMETA_URL, URLMETA_EMAIL, URLMETA_API_TOKEN, \
    MAX_PARALLEL_REQUESTS
from models.db.article import Article
from models.db.post import Post


def get_text_from_article_url(article_url: str) -> str:
    res = requests.get(f'{EXTRACTOR_URL}/?apikey={EXTRACTOR_API_TOKEN}&url={article_url}')
    res.raise_for_status()
    return res.json()['text']


def get_image_url_from_article_url(article_url: str) -> str:
    encoded_token = f'{URLMETA_EMAIL}:{URLMETA_API_TOKEN}'.encode('ascii')
    token_b64_str = base64.b64encode(encoded_token).decode('ascii')
    # TODO: There's a better way to generate the auth token
    res = requests.get(f'{URLMETA_URL}/?url={article_url}',
                       headers={'Authorization': f'Basic {token_b64_str}'})
    res.raise_for_status()
    return res.json()['meta']['image']


def generate_article_from_post(post: Post):
    try:
        print(f'Generating article for post {post.title}')
        text = get_text_from_article_url(post.url)
        image = get_image_url_from_article_url(post.url)
        new_article = Article(post_id=post.id, title=post.title, text=text, url=post.url,
                              image_url=image, score=post.score, subreddit=post.subreddit)
        session_object.add(new_article)
    except Exception as e:
        print(f'Failed to generate article for post {post.title}. The following error was received: {e}')
        # TODO: Add a better log


def generate_articles():
    current_posts = session_object.query(Post).all()
    with ThreadPool(MAX_PARALLEL_REQUESTS) as pool:
        pool.map(generate_article_from_post, current_posts)
    session_object.commit()
