from typing import Literal
from pydantic import Field
from schemaorg_models.news_article import NewsArticle


class ReviewNewsArticle(NewsArticle):
    """
A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work.
    """
    class_: Literal['https://schema.org/ReviewNewsArticle'] = Field('class', alias='class', serialization_alias='class') # type: ignore
