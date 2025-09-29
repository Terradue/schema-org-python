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
from .broadcast_service import BroadcastService

class RadioBroadcastService(BroadcastService):
    '''
    A delivery service through which radio content is provided via broadcast over the air or online.
    '''
    class_: Literal['https://schema.org/RadioBroadcastService'] = Field( # type: ignore
        default='https://schema.org/RadioBroadcastService',
        alias='@type',
        serialization_alias='@type'
    )
