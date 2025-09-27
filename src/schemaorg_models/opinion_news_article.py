from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.news_article import NewsArticle


class OpinionNewsArticle(NewsArticle):
    """
An [[OpinionNewsArticle]] is a [[NewsArticle]] that primarily expresses opinions rather than journalistic reporting of news and events. For example, a [[NewsArticle]] consisting of a column or [[Blog]]/[[BlogPosting]] entry in the Opinions section of a news publication. 
    """
    type_: Literal['https://schema.org/OpinionNewsArticle'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OpinionNewsArticle'),serialization_alias='class') # type: ignore
