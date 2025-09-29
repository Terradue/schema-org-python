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
from .audio_object import AudioObject

class AudioObjectSnapshot(AudioObject):
    '''
    A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.
    '''
    class_: Literal['https://schema.org/AudioObjectSnapshot'] = Field( # type: ignore
        default='https://schema.org/AudioObjectSnapshot',
        alias='@type',
        serialization_alias='@type'
    )
