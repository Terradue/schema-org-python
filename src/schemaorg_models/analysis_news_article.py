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

class AnalysisNewsArticle(NewsArticle):
    '''
    An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions.
    '''
    class_: Literal['https://schema.org/AnalysisNewsArticle'] = Field( # type: ignore
        default='https://schema.org/AnalysisNewsArticle',
        alias='@type',
        serialization_alias='@type'
    )
