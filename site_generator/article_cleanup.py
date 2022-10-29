from models.website.website import WebsiteArticle, Website

texts_to_remove = [
    "IE 11 is not supported. For an optimal experience visit our site on another browser.",
    "IE 11 is not supported.",
    "Please refresh the page or navigate to another page on the site to be automatically logged in",
    "Please refresh your browser to be logged in",
    "Sign up to comment and more",
    "Share this item on Facebook",
]


def cleanup_article(article: WebsiteArticle):
    for text in texts_to_remove:
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
