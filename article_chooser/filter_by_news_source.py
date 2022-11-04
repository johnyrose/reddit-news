from typing import List

from common.static_texts.blocked_news_sources import BLOCKED_NEWS_SOURCES
from models.website.website import WebsiteArticle


def is_article_from_blocked_news_source(article: WebsiteArticle) -> bool:
    for source in BLOCKED_NEWS_SOURCES:
        if source in article.url:
            return True
    return False


def filter_out_articles_from_blocked_news_sources(articles: List[WebsiteArticle]) -> List[WebsiteArticle]:
    return [article for article in articles if not is_article_from_blocked_news_source(article)]
