from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.media_gallery import MediaGallery


class ImageGallery(MediaGallery):
    """
Web page type: Image gallery page.
    """
    type_: Literal['https://schema.org/ImageGallery'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ImageGallery'),serialization_alias='class') # type: ignore
