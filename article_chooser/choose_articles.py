from typing import List

from article_chooser.articles_sorting import sort_articles_by_score, sort_articles_by_relative_upvotes
from article_chooser.filter_by_news_source import filter_out_articles_from_blocked_news_sources
from article_chooser.subreddit_data import get_list_of_subreddits_with_articles, get_articles_for_subreddit
from common.db_connector import session_object
from common.logger import logger
from common.settings import MINIMUM_ARTICLES_AMOUNT_WARNING, SUB_ARTICLES_AMOUNT, MINI_ARTICLES_AMOUNT, \
    NEWS_ROW_ARTICLE_AMOUNT, SORTING_METHOD
from models.db.article import Article
from models.website.sorting_method import SortingMethod
from models.website.website import Website, NewsRow, WebsiteArticle


def generate_news_rows(articles: List[WebsiteArticle], website: Website):
    subreddits = get_list_of_subreddits_with_articles(articles)
    for subreddit in subreddits:
        subreddit_articles = get_articles_for_subreddit(subreddit, articles)
        unused_subreddit_articles = [article for article in
                                     subreddit_articles if not website.is_article_in_website(article)]
        unused_subreddit_articles = sort_articles_by_score(unused_subreddit_articles)
        news_row = NewsRow(name=subreddit, articles=unused_subreddit_articles[:NEWS_ROW_ARTICLE_AMOUNT])
        website.news_rows.append(news_row)


def sort_articles_by_chosen_method(articles: List[WebsiteArticle]) -> List[WebsiteArticle]:
    if SORTING_METHOD == SortingMethod.score:
        return sort_articles_by_score(articles)
    else:
        return sort_articles_by_relative_upvotes(articles)


def choose_articles() -> Website:
    db_articles: List[Article] = session_object.query(Article).all()
    if len(db_articles) < MINIMUM_ARTICLES_AMOUNT_WARNING:
        logger.warning(f'Too few articles: you have less than {MINIMUM_ARTICLES_AMOUNT_WARNING} articles in '
                       f'the database, which means that the website might be broken.')
    current_articles: List[WebsiteArticle] = [WebsiteArticle.from_db_article(article) for article in db_articles]
    current_articles = filter_out_articles_from_blocked_news_sources(current_articles)
    sorted_articles = sort_articles_by_chosen_method(current_articles)
    main_article = sorted_articles[0]
    website = Website(main_article=main_article, sub_articles=[], mini_articles=[], news_rows=[])
    website.sub_articles = sorted_articles[1:SUB_ARTICLES_AMOUNT + 1]
    website.mini_articles = sorted_articles[SUB_ARTICLES_AMOUNT + 1: SUB_ARTICLES_AMOUNT + MINI_ARTICLES_AMOUNT + 1]
    generate_news_rows(sorted_articles, website)
    return website
