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
from .enumeration import Enumeration

class MusicAlbumReleaseType(Enumeration):
    '''
    The kind of release which this album is: single, EP or album.
    '''
    class_: Literal['https://schema.org/MusicAlbumReleaseType'] = Field( # type: ignore
        default='https://schema.org/MusicAlbumReleaseType',
        alias='@type',
        serialization_alias='@type'
    )
