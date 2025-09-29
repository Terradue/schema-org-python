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

class MusicReleaseFormatType(Enumeration):
    '''
    Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).
    '''
    class_: Literal['https://schema.org/MusicReleaseFormatType'] = Field( # type: ignore
        default='https://schema.org/MusicReleaseFormatType',
        alias='@type',
        serialization_alias='@type'
    )
