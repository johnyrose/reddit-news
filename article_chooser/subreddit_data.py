from typing import List

from models.website.website import WebsiteArticle


def get_list_of_subreddits_with_articles(articles: List[WebsiteArticle]) -> List[str]:
    return list(set([article.subreddit for article in articles]))


def get_articles_for_subreddit(subreddit: str, articles: List[WebsiteArticle]) -> List[WebsiteArticle]:
    return [article for article in articles if article.subreddit == subreddit]
