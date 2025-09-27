from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.news_article import NewsArticle


class ReviewNewsArticle(NewsArticle):
    """
A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work.
    """
    type_: Literal['https://schema.org/ReviewNewsArticle'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ReviewNewsArticle'),serialization_alias='class') # type: ignore
