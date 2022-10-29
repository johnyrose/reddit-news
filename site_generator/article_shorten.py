from models.website.website import WebsiteArticle, Website


def shorten_article_text(article: WebsiteArticle, max_length: int):
    if len(article.text) > max_length:
        article.text = article.text[:max_length] + '...'


def shorten_website_articles(website: Website):
    # TODO: Don't use magic numbers, store them in the config
    shorten_article_text(website.main_article, 600)
    for article in website.sub_articles:
        shorten_article_text(article, 250)
    for article in website.mini_articles:
        shorten_article_text(article, 100)
    for news_row in website.news_rows:
        for article in news_row.articles:
            shorten_article_text(article, 200)

