from typing import Literal
from pydantic import Field
from schemaorg_models.collection_page import CollectionPage


class MediaGallery(CollectionPage):
    """
Web page type: Media gallery page. A mixed-media page that can contain media such as images, videos, and other multimedia.
    """
    class_: Literal['https://schema.org/MediaGallery'] = Field('class', alias='class', serialization_alias='class') # type: ignore
