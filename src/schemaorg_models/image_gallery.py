from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .media_gallery import MediaGallery

class ImageGallery(MediaGallery):
    '''
    Web page type: Image gallery page.
    '''
    class_: Literal['https://schema.org/ImageGallery'] = Field( # type: ignore
        default='https://schema.org/ImageGallery',
        alias='@type',
        serialization_alias='@type'
    )
