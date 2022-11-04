from typing import List

from models.website.website import WebsiteArticle

blocked_news_sources = [
    "facteroid.com",  # Blocked due to no images in articles
    "www.reuters.com"  # Blocked due to no images in articles
]


def is_article_from_blocked_news_source(article: WebsiteArticle) -> bool:
    for source in blocked_news_sources:
        if source in article.url:
            return True
    return False


def filter_out_articles_from_blocked_news_sources(articles: List[WebsiteArticle]) -> List[WebsiteArticle]:
    return [article for article in articles if not is_article_from_blocked_news_source(article)]
