import jinja2

from common.settings import TEMPLATE_FILE, OUTPUT_FILE
from common.logger import logger
from models.website.website import Website
from site_generator.article_cleanup import cleanup_website_articles
from site_generator.article_shorten import shorten_website_articles


def generate_site(website: Website):
    env = jinja2.Environment()
    template_file_content = open(TEMPLATE_FILE).read()
    template = env.from_string(template_file_content)
    cleanup_website_articles(website)
    shorten_website_articles(website)

    main_article = website.main_article.dict()
    sub_articles = [article.dict() for article in website.sub_articles]
    mini_articles = [article.dict() for article in website.mini_articles]
    news_rows = [news_row.dict() for news_row in website.news_rows]

    output = template.render(main_article=main_article,
                             sub_articles=sub_articles,
                             mini_articles=mini_articles,
                             news_rows=news_rows)
    open(OUTPUT_FILE, 'w', encoding='utf-8').write(output)
    logger.info(f'Website generation complete. Output file: {OUTPUT_FILE}')
