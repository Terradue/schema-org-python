from typing import Literal
from pydantic import Field
from schemaorg_models.media_gallery import MediaGallery


class ImageGallery(MediaGallery):
    """
Web page type: Image gallery page.
    """
    class_: Literal['https://schema.org/ImageGallery'] = Field(default='https://schema.org/ImageGallery', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
