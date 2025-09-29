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
from .visual_artwork import VisualArtwork

class CoverArt(VisualArtwork):
    '''
    The artwork on the outer surface of a CreativeWork.
    '''
    class_: Literal['https://schema.org/CoverArt'] = Field( # type: ignore
        default='https://schema.org/CoverArt',
        alias='@type',
        serialization_alias='@type'
    )
