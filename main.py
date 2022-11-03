from article_chooser.choose_articles import choose_articles
from article_generator.generate_articles import generate_articles
from collector import collect_subreddits
from common.logger import logger
from common.db_connector import Base, db_engine
from site_generator.generate_site import generate_site

if __name__ == '__main__':
    Base.metadata.create_all(db_engine)
    # logger.info('Collecting subreddits...')
    # collect_subreddits()
    # logger.info('Generating articles...')
    # generate_articles()
    logger.info('Choosing articles...')
    website = choose_articles()
    logger.info('Generating site...')
    generate_site(website)
