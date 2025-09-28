from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .article import Article

class AdvertiserContentArticle(Article):
    """
An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content.
    """
    class_: Literal['https://schema.org/AdvertiserContentArticle'] = Field( # type: ignore
        default='https://schema.org/AdvertiserContentArticle',
        alias='@type',
        serialization_alias='@type'
    )
