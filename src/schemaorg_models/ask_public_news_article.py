from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.news_article import NewsArticle


class AskPublicNewsArticle(NewsArticle):
    """
A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the public for input, insights, clarifications, anecdotes, documentation, etc., on an issue, for reporting purposes.
    """
    type_: Literal['https://schema.org/AskPublicNewsArticle'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AskPublicNewsArticle'),serialization_alias='class') # type: ignore
