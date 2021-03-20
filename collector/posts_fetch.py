import praw


def fetch_posts(reddit_client: praw.Reddit, subreddit: str, posts_amount: int, ignore_stickied: bool):
    subreddit = reddit_client.subreddit(subreddit)
    posts = subreddit.hot(limit=posts_amount)
    if ignore_stickied:
        return [post for post in posts if not post.stickied]
    return posts
