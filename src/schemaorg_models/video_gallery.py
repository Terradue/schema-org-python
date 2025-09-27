from typing import Literal
from pydantic import Field
from schemaorg_models.media_gallery import MediaGallery


class VideoGallery(MediaGallery):
    """
Web page type: Video gallery page.
    """
    class_: Literal['https://schema.org/VideoGallery'] = Field(default='https://schema.org/VideoGallery', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
