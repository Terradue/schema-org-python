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

class VideoGallery(MediaGallery):
    '''
    Web page type: Video gallery page.
    '''
    class_: Literal['https://schema.org/VideoGallery'] = Field( # type: ignore
        default='https://schema.org/VideoGallery',
        alias='@type',
        serialization_alias='@type'
    )
