from typing import Literal
from pydantic import Field
from schemaorg_models.news_article import NewsArticle


class AskPublicNewsArticle(NewsArticle):
    """
A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the public for input, insights, clarifications, anecdotes, documentation, etc., on an issue, for reporting purposes.
    """
    type_: Literal['https://schema.org/AskPublicNewsArticle'] = Field(default='https://schema.org/AskPublicNewsArticle', alias='@type', serialization_alias='@type') # type: ignore
