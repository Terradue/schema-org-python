from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.article import Article


class ScholarlyArticle(Article):
    """
A scholarly article.
    """
    type_: Literal['https://schema.org/ScholarlyArticle'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ScholarlyArticle'),serialization_alias='class') # type: ignore
