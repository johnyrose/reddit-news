from typing import List

from pydantic import BaseModel

from models.db.article import Article


class WebsiteArticle(BaseModel):
    id: int
    score: int
    post_id: str
    title: str
    text: str
    url: str
    image_url: str
    subreddit: str

    @classmethod
    def from_db_article(cls, article: Article):
        return cls(
            id=article.id,
            score=article.score,
            post_id=article.post_id,
            title=article.title,
            text=article.text,
            url=article.url,
            image_url=article.image_url,
            subreddit=article.subreddit
        )


class NewsRow(BaseModel):
    name: str
    articles: List[WebsiteArticle]  # Max length of 3


class Website(BaseModel):
    main_article: WebsiteArticle
    sub_articles: List[WebsiteArticle]  # Should not be more than 3
    mini_articles: List[WebsiteArticle]  # Should not be more than 4
    news_rows: List[NewsRow]

    def is_article_in_website(self, article: WebsiteArticle) -> bool:
        if article == self.main_article:
            return True
        if article in self.sub_articles:
            return True
        if article in self.mini_articles:
            return True
        for news_row in self.news_rows:
            if article in news_row.articles:
                return True
        return False
