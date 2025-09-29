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

class SatiricalArticle(Article):
    '''
    An [[Article]] whose content is primarily [[satirical]](https://en.wikipedia.org/wiki/Satire) in nature, i.e. unlikely to be literally true. A satirical article is sometimes but not necessarily also a [[NewsArticle]]. [[ScholarlyArticle]]s are also sometimes satirized.
    '''
    class_: Literal['https://schema.org/SatiricalArticle'] = Field( # type: ignore
        default='https://schema.org/SatiricalArticle',
        alias='@type',
        serialization_alias='@type'
    )
