from models.website.website import WebsiteArticle, Website

texts_to_remove = [
    "IE 11 is not supported. For an optimal experience visit our site on another browser.",
    "IE 11 is not supported.",
    "Please refresh the page or navigate to another page on the site to be automatically logged in",
    "Please refresh your browser to be logged in",
    "Sign up to comment and more",
    "Share this item on Facebook",
    "We've made some important changes to our Privacy and Cookies Policy and we want you to know what this means for "
    "you and your data. We and our partners use technologies, such as cookies, and collect browsing data to give you"
    " the best online experience and to personalise the content and advertising shown to you. Please let us know if "
    "you agree. These settings apply to AMP pages only. You may be asked to set these preferences again when you visit"
    " non-AMP BBC pages. The lightweight mobile page you have visited has been built using Google AMP technology. "
    "To make our web pages work, we store some limited information on your device without your consent. We use local "
    "storage to store your consent preferences on your device. When you consent to data collection on AMP pages you"
    " are consenting to allow us to display personalised ads that are relevant to you when you are outside of the UK."
    " You can choose not to receive personalised ads by clicking \"Reject data collection and continue\" below. Please "
    "note that you will still see advertising, but it will not be personalised to you. You can change these settings "
    "by clicking \"Ad Choices / Do not sell my info\" in the footer at any time.",
    "Send any friend a story"
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
