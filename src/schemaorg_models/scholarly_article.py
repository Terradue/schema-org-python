from __future__ import annotations

from .article import Article    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ScholarlyArticle(Article):
    """
A scholarly article.
    """
    class_: Literal['https://schema.org/ScholarlyArticle'] = Field( # type: ignore
        default='https://schema.org/ScholarlyArticle',
        alias='@type',
        serialization_alias='@type'
    )
