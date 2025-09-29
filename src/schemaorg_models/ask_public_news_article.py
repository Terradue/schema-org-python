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

class AskPublicNewsArticle(NewsArticle):
    '''
    A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the public for input, insights, clarifications, anecdotes, documentation, etc., on an issue, for reporting purposes.
    '''
    class_: Literal['https://schema.org/AskPublicNewsArticle'] = Field( # type: ignore
        default='https://schema.org/AskPublicNewsArticle',
        alias='@type',
        serialization_alias='@type'
    )
