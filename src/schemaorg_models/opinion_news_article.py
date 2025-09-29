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

class OpinionNewsArticle(NewsArticle):
    '''
    An [[OpinionNewsArticle]] is a [[NewsArticle]] that primarily expresses opinions rather than journalistic reporting of news and events. For example, a [[NewsArticle]] consisting of a column or [[Blog]]/[[BlogPosting]] entry in the Opinions section of a news publication. 
    '''
    class_: Literal['https://schema.org/OpinionNewsArticle'] = Field( # type: ignore
        default='https://schema.org/OpinionNewsArticle',
        alias='@type',
        serialization_alias='@type'
    )
