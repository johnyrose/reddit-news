from typing import List

from article_chooser.subreddit_data import get_list_of_subreddits_with_articles, get_articles_for_subreddit
from models.website.website import WebsiteArticle


def sort_articles_by_score(articles: List[WebsiteArticle]) -> List[WebsiteArticle]:
    return sorted(articles, key=lambda article: article.score, reverse=True)


def get_subreddit_articles_with_new_scores(articles: List[WebsiteArticle], subreddit: str) -> List[WebsiteArticle]:
    subreddit_articles = get_articles_for_subreddit(subreddit, articles)
    total_subreddit_upvotes = sum([article.score for article in subreddit_articles])
    for article in subreddit_articles:
        article.score = article.score / total_subreddit_upvotes
    return subreddit_articles


def sort_articles_by_relative_upvotes(articles: List[WebsiteArticle]) -> List[WebsiteArticle]:
    """
    This method sorts articles by their relative upvotes to the total sum of upvotes from the same subreddit.
    That means that if there are 3 articles from the same subreddit, with 100, 50 and 25 upvotes, the first one will
    have a 100/175 = 0.57 score, the second one will have a 50/175 = 0.29 score and so on.

    This is an attempt to spread the articles more evenly between the subreddit and prevent the website from having
    too many articles from the same subreddit on the top of the page.

    Of course this is by no means perfect, and I'd suggest trying it only if you are not satisfied with the result with
    the other method (which is simply sorting by upvotes).
    """
    subreddits = get_list_of_subreddits_with_articles(articles)
    modified_articles = []
    for subreddit in subreddits:
        articles_with_new_score = get_subreddit_articles_with_new_scores(articles, subreddit)
        modified_articles.extend(articles_with_new_score)
    sort_articles_by_score(modified_articles)
    return modified_articles
