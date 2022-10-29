from common.settings import MAIN_ARTICLES_MAX_LENGTH, SUB_ARTICLES_MAX_LENGTH, MINI_ARTICLES_MAX_LENGTH, \
    NEWS_ROW_MAX_LENGTH, TITLES_MAX_LENGTH
from models.website.website import WebsiteArticle, Website


def shorten_article_texts(article: WebsiteArticle, max_text_length: int):
    if len(article.text) > max_text_length:
        article.text = article.text[:max_text_length] + '...'
    if len(article.title) > TITLES_MAX_LENGTH:
        article.title = article.title[:TITLES_MAX_LENGTH] + '...'


def shorten_website_articles(website: Website):
    shorten_article_texts(website.main_article, MAIN_ARTICLES_MAX_LENGTH)
    for article in website.sub_articles:
        shorten_article_texts(article, SUB_ARTICLES_MAX_LENGTH)
    for article in website.mini_articles:
        shorten_article_texts(article, MINI_ARTICLES_MAX_LENGTH)
    for news_row in website.news_rows:
        for article in news_row.articles:
            shorten_article_texts(article, NEWS_ROW_MAX_LENGTH)

