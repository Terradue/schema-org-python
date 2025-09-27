from typing import Literal
from pydantic import Field
from schemaorg_models.news_article import NewsArticle


class ReviewNewsArticle(NewsArticle):
    """
A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work.
    """
    class_: Literal['https://schema.org/ReviewNewsArticle'] = Field(default='https://schema.org/ReviewNewsArticle', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
