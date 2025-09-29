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

class RadioChannel(BroadcastChannel):
    '''
    A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.
    '''
    class_: Literal['https://schema.org/RadioChannel'] = Field( # type: ignore
        default='https://schema.org/RadioChannel',
        alias='@type',
        serialization_alias='@type'
    )
