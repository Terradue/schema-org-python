from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.news_article import NewsArticle

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OpinionNewsArticle(NewsArticle):
    """
An [[OpinionNewsArticle]] is a [[NewsArticle]] that primarily expresses opinions rather than journalistic reporting of news and events. For example, a [[NewsArticle]] consisting of a column or [[Blog]]/[[BlogPosting]] entry in the Opinions section of a news publication. 
    """
    class_: Literal['https://schema.org/OpinionNewsArticle'] = Field( # type: ignore
        default='https://schema.org/OpinionNewsArticle',
        alias='@type',
        serialization_alias='@type'
    )
