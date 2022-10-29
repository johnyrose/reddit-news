from typing import List

from pydantic import BaseModel

from models.db.article import Article


class NewsRow(BaseModel):
    name: str
    articles = List[Article]  # Max length of 3


class Website(BaseModel):
    main_article: Article
    sub_articles: List[Article]  # Should not be more than 3
    mini_articles: List[Article]  # Should not be more than 4
    news_rows: List[NewsRow]

    def is_article_in_website(self, article: Article) -> bool:
        if article in self.sub_articles:
            return True
        if article in self.mini_articles:
            return True
        for news_row in self.news_rows:
            if article in news_row.articles:
                return True
        return False
