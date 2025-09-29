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
from .radio_channel import RadioChannel

class AMRadioChannel(RadioChannel):
    '''
    A radio channel that uses AM.
    '''
    class_: Literal['https://schema.org/AMRadioChannel'] = Field( # type: ignore
        default='https://schema.org/AMRadioChannel',
        alias='@type',
        serialization_alias='@type'
    )
