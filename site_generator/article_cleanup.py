from common.static_texts.texts_to_remove import TEXTS_TO_REMOVE
from models.website.website import WebsiteArticle, Website


def cleanup_article(article: WebsiteArticle):
    for text in TEXTS_TO_REMOVE:
        if text in article.text:
            article.text = article.text.replace(text, "")


def cleanup_website_articles(website: Website):
    """
    This function aims to remove specific familiar texts that are most likely irrelevant. It's a dirty hack,
    but it's better than not doing it.
    """
    cleanup_article(website.main_article)
    for article in website.sub_articles:
        cleanup_article(article)
    for article in website.mini_articles:
        cleanup_article(article)
    for news_row in website.news_rows:
        for article in news_row.articles:
            cleanup_article(article)
