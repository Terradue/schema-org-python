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
from .article import Article

class ScholarlyArticle(Article):
    '''
    A scholarly article.
    '''
    class_: Literal['https://schema.org/ScholarlyArticle'] = Field( # type: ignore
        default='https://schema.org/ScholarlyArticle',
        alias='@type',
        serialization_alias='@type'
    )
