from typing import Literal
from pydantic import Field
from schemaorg_models.article import Article


class AdvertiserContentArticle(Article):
    """
An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content.
    """
    class_: Literal['https://schema.org/AdvertiserContentArticle'] = Field(default='https://schema.org/AdvertiserContentArticle', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
