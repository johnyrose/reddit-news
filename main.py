import os
from article_chooser.choose_articles import choose_articles
from article_generator.generate_articles import generate_articles
from collector import collect_subreddits
from common.logger import logger
from common.db_connector import Base, db_engine
from common.settings import PERFORM_DATA_COLLECTION, PERFORM_WEBSITE_GENERATION, DB_FILE
from site_generator.generate_site import generate_site


def check_for_existing_db_file():
    if os.path.exists(DB_FILE):
        logger.warning(f'SQLITE file {DB_FILE} already exists. This might cause duplicates or older articles to'
                       f' appear. If you want a clean slate, it is recommended to delete this file and run the '
                       f'process again.')


def main():
    Base.metadata.create_all(db_engine)
    if PERFORM_DATA_COLLECTION:
        check_for_existing_db_file()
        logger.info('Collecting subreddits...')
        collect_subreddits()
        logger.info('Generating articles...')
        generate_articles()
    else:
        logger.info('Data collection is disabled, skipping...')
    if PERFORM_WEBSITE_GENERATION:
        logger.info('Choosing articles...')
        website = choose_articles()
        logger.info('Generating site...')
        generate_site(website)
    else:
        logger.info('Website generation is disabled, skipping...')


if __name__ == '__main__':
    main()
