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
from .broadcast_channel import BroadcastChannel

class TelevisionChannel(BroadcastChannel):
    '''
    A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.
    '''
    class_: Literal['https://schema.org/TelevisionChannel'] = Field( # type: ignore
        default='https://schema.org/TelevisionChannel',
        alias='@type',
        serialization_alias='@type'
    )
