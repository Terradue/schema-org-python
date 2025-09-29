from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .news_article import NewsArticle

class ReviewNewsArticle(NewsArticle):
    '''
    A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work.
    '''
    class_: Literal['https://schema.org/ReviewNewsArticle'] = Field( # type: ignore
        default='https://schema.org/ReviewNewsArticle',
        alias='@type',
        serialization_alias='@type'
    )
