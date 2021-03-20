import settings
import praw
import schedule
import time
from sqlalchemy import create_engine
from fetch_posts import fetch_posts


def save_subreddit(client: praw.Reddit, config: dict):
    posts = fetch_posts(reddit_client=client,
                        subreddit=config['name'],
                        posts_amount=config['posts'],
                        ignore_stickied=config['ignoreStickied'])
    print(posts)


if __name__ == "__main__":
    db_engine = create_engine('sqlite:///:./db.sqlite', echo=True)
    reddit_client = praw.Reddit(
        client_id=settings.REDDIT_CLIENT_ID,
        client_secret=settings.REDDIT_CLIENT_SECRET,
        username=settings.REDDIT_USER,
        password=settings.REDDIT_PASSWORD,
        user_agent=settings.REDDIT_USER_AGENT
    )
    for subreddit_config in settings.SUBREDDITS_CONFIG:
        schedule.every(subreddit_config['secondsInterval']).seconds.do(save_subreddit, reddit_client, subreddit_config)
    while True:
        schedule.run_pending()
        time.sleep(1)
