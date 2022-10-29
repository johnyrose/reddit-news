from article_chooser.choose_articles import choose_articles
from article_generator.generate_articles import generate_articles
from collector import collect_subreddits
from common.db_connector import Base, db_engine
from site_generator.generate_site import generate_site

if __name__ == '__main__':
    Base.metadata.create_all(db_engine)
    print('Collecting subreddits...')
    collect_subreddits()
    print('Generating articles...')
    generate_articles()
    print('Choosing articles...')
    website = choose_articles()
    print('Generating site...')
    generate_site(website)
