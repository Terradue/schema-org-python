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
from .collection_page import CollectionPage

class MediaGallery(CollectionPage):
    '''
    Web page type: Media gallery page. A mixed-media page that can contain media such as images, videos, and other multimedia.
    '''
    class_: Literal['https://schema.org/MediaGallery'] = Field( # type: ignore
        default='https://schema.org/MediaGallery',
        alias='@type',
        serialization_alias='@type'
    )
