from typing import List

from common.db_connector import session_object
from models.db.article import Article


def sort_articles_by_upvotes(articles: List[Article]) -> List[Article]:
    return sorted(articles, key=lambda article: article.post.upvotes, reverse=True)


def choose_articles():
    current_articles: List[Article] = session_object.query(Article).all()  # TODO: Don't fetch all articles
