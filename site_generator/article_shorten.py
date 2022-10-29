from common.settings import MAIN_ARTICLES_MAX_LENGTH, SUB_ARTICLES_MAX_LENGTH, MINI_ARTICLES_MAX_LENGTH, \
    NEWS_ROW_MAX_LENGTH
from models.website.website import WebsiteArticle, Website


def shorten_article_text(article: WebsiteArticle, max_length: int):
    if len(article.text) > max_length:
        article.text = article.text[:max_length] + '...'


def shorten_website_articles(website: Website):
    shorten_article_text(website.main_article, MAIN_ARTICLES_MAX_LENGTH)
    for article in website.sub_articles:
        shorten_article_text(article, SUB_ARTICLES_MAX_LENGTH)
    for article in website.mini_articles:
        shorten_article_text(article, MINI_ARTICLES_MAX_LENGTH)
    for news_row in website.news_rows:
        for article in news_row.articles:
            shorten_article_text(article, NEWS_ROW_MAX_LENGTH)

