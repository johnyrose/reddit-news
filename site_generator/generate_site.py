import jinja2
import sys
from models.website.website import Website, WebsiteArticle


def shorten_article_text(article: WebsiteArticle, max_length: int):
    if len(article.text) > max_length:
        article.text = article.text[:max_length] + '...'


def shorten_articles(website: Website):
    # TODO: Don't use magic numbers, store them in the config
    shorten_article_text(website.main_article, 600)
    for article in website.sub_articles:
        shorten_article_text(article, 250)
    for article in website.mini_articles:
        shorten_article_text(article, 100)
    for news_row in website.news_rows:
        for article in news_row.articles:
            shorten_article_text(article, 200)


def generate_site(website: Website):
    env = jinja2.Environment()
    template_file_content = open('site_generator/template.html').read()
    template = env.from_string(template_file_content)
    shorten_articles(website)
    main_article = website.main_article.dict()
    sub_articles = [article.dict() for article in website.sub_articles]
    mini_articles = [article.dict() for article in website.mini_articles]
    news_rows = [news_row.dict() for news_row in website.news_rows]

    output = template.render(main_article=main_article,
                             sub_articles=sub_articles,
                             mini_articles=mini_articles,
                             news_rows=news_rows)
    open('site_generator/output.html', 'w').write(output)
