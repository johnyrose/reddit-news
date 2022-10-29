from typing import List

from common.db_connector import session_object
from models.db.article import Article
from models.website.website import Website


def sort_articles_by_upvotes(articles: List[Article]) -> List[Article]:
    return sorted(articles, key=lambda article: article.post.upvotes, reverse=True)


def get_list_of_subreddits_with_articles(articles: List[Article]) -> List[str]:
    return list(set([article.post.subreddit for article in articles]))


def get_articles_for_subreddit(subreddit: str, articles: List[Article]) -> List[Article]:
    return [article for article in articles if article.post.subreddit == subreddit]


# def generate_sub_articles(sorted_articles: List[Article]) -> List[Article]:
#     sorted_articles = sort_articles_by_upvotes(articles)
#     used_articles = []
#     main_article = sorted_articles[0]
#     sub_articles = sorted_articles[1:4]
#     mini_articles = sorted_articles[4:8]
#     used_articles.append(main_article)
#     used_articles.extend(sub_articles)
#     used_articles.extend(mini_articles)


def choose_articles():
    current_articles: List[Article] = session_object.query(Article).all()  # TODO: Don't fetch all articles
    sorted_articles = sort_articles_by_upvotes(current_articles)
    main_article = sorted_articles[0]
    website = Website(main_article=main_article, sub_articles=[], mini_articles=[], news_rows=[])