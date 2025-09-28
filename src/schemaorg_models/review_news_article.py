from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .news_article import NewsArticle

class ReviewNewsArticle(NewsArticle):
    """
A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work.
    """
    class_: Literal['https://schema.org/ReviewNewsArticle'] = Field( # type: ignore
        default='https://schema.org/ReviewNewsArticle',
        alias='@type',
        serialization_alias='@type'
    )
