from typing import Literal
from pydantic import Field
from schemaorg_models.collection_page import CollectionPage


class MediaGallery(CollectionPage):
    """
Web page type: Media gallery page. A mixed-media page that can contain media such as images, videos, and other multimedia.
    """
    type_: Literal['https://schema.org/MediaGallery'] = Field(default='https://schema.org/MediaGallery', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
