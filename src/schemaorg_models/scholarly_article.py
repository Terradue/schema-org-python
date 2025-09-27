from typing import Literal
from pydantic import Field
from schemaorg_models.article import Article


class ScholarlyArticle(Article):
    """
A scholarly article.
    """
    class_: Literal['https://schema.org/ScholarlyArticle'] = Field(default='https://schema.org/ScholarlyArticle', alias='@type', serialization_alias='@type') # type: ignore
