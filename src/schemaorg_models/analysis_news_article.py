from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.news_article import NewsArticle


class AnalysisNewsArticle(NewsArticle):
    """
An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions.
    """
    type_: Literal['https://schema.org/AnalysisNewsArticle'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AnalysisNewsArticle'),serialization_alias='class') # type: ignore
