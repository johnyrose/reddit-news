import requests

from common.db_connector import session_object
from common.settings import EXTRACTOR_URL, EXTRACTOR_API_TOKEN
from models.article import Article
from models.post import Post


def get_text_from_article_url(article_url: str) -> str:
    res = requests.get(f'{EXTRACTOR_URL}/?apikey={EXTRACTOR_API_TOKEN}&url={article_url}')
    res.raise_for_status()
    return res.json()['text']


def generate_articles():
    current_posts = session_object.query(Post).all()
    for post in current_posts:
        try:
            text = get_text_from_article_url(post.url)
            new_article = Article(post_id=post.id, title=post.title, text=text, url=post.url,
                                  image_url=post.image_url)
            session_object.add(new_article)
            session_object.commit()
        except Exception as e:
            print(f'Failed to generate article for post {post.title}. The following error was received: {e}')
            # TODO: Add a better log
