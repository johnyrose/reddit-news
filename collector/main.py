import settings
import praw

if __name__ == "__main__":
    reddit_client = praw.Reddit(
        client_id=settings.REDDIT_CLIENT_ID,
        client_secret=settings.REDDIT_CLIENT_SECRET,
        username=settings.REDDIT_USER,
        password=settings.REDDIT_PASSWORD,
        user_agent=settings.REDDIT_USER_AGENT
    )
