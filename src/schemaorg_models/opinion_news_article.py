from typing import Literal
from pydantic import Field
from schemaorg_models.news_article import NewsArticle


class OpinionNewsArticle(NewsArticle):
    """
An [[OpinionNewsArticle]] is a [[NewsArticle]] that primarily expresses opinions rather than journalistic reporting of news and events. For example, a [[NewsArticle]] consisting of a column or [[Blog]]/[[BlogPosting]] entry in the Opinions section of a news publication. 
    """
    class_: Literal['https://schema.org/OpinionNewsArticle'] = Field(default='https://schema.org/OpinionNewsArticle', alias='@type', serialization_alias='@type') # type: ignore
