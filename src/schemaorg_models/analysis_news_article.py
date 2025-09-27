from typing import Literal
from pydantic import Field
from schemaorg_models.news_article import NewsArticle


class AnalysisNewsArticle(NewsArticle):
    """
An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions.
    """
    class_: Literal['https://schema.org/AnalysisNewsArticle'] = Field(default='https://schema.org/AnalysisNewsArticle', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
