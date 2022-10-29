from typing import List

from common.db_connector import session_object
from models.db.article import Article
from models.website.website import Website, NewsRow


def sort_articles_by_upvotes(articles: List[Article]) -> List[Article]:
    return sorted(articles, key=lambda article: article.post.upvotes, reverse=True)


def get_list_of_subreddits_with_articles(articles: List[Article]) -> List[str]:
    return list(set([article.post.subreddit for article in articles]))


def get_articles_for_subreddit(subreddit: str, articles: List[Article]) -> List[Article]:
    return [article for article in articles if article.post.subreddit == subreddit]


def generate_news_rows(articles: List[Article], website: Website):
    subreddits = get_list_of_subreddits_with_articles(articles)
    for subreddit in subreddits:
        subreddit_articles = get_articles_for_subreddit(subreddit, articles)
        unused_subreddit_articles = [article for article in
                                     subreddit_articles if not website.is_article_in_website(article)]
        unused_subreddit_articles = sort_articles_by_upvotes(unused_subreddit_articles)
        news_row = NewsRow(name=subreddit, articles=unused_subreddit_articles[:3])
        website.news_rows.append(news_row)


def choose_articles() -> Website:
    current_articles: List[Article] = session_object.query(Article).all()  # TODO: Don't fetch all articles
    sorted_articles = sort_articles_by_upvotes(current_articles)
    main_article = sorted_articles[0]
    website = Website(main_article=main_article, sub_articles=[], mini_articles=[], news_rows=[])
    website.sub_articles = sorted_articles[1:4]
    website.mini_articles = sorted_articles[4:8]
    generate_news_rows(sorted_articles, website)
    return website
