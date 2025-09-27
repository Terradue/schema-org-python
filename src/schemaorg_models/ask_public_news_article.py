from typing import Literal
from pydantic import Field
from schemaorg_models.news_article import NewsArticle


class AskPublicNewsArticle(NewsArticle):
    """
A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the public for input, insights, clarifications, anecdotes, documentation, etc., on an issue, for reporting purposes.
    """
    class_: Literal['https://schema.org/AskPublicNewsArticle'] = Field('class', alias='class', serialization_alias='class') # type: ignore
