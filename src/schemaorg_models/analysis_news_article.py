from __future__ import annotations

from .news_article import NewsArticle    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AnalysisNewsArticle(NewsArticle):
    """
An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions.
    """
    class_: Literal['https://schema.org/AnalysisNewsArticle'] = Field( # type: ignore
        default='https://schema.org/AnalysisNewsArticle',
        alias='@type',
        serialization_alias='@type'
    )
