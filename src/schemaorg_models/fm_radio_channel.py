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

class FMRadioChannel(RadioChannel):
    '''
    A radio channel that uses FM.
    '''
    class_: Literal['https://schema.org/FMRadioChannel'] = Field( # type: ignore
        default='https://schema.org/FMRadioChannel',
        alias='@type',
        serialization_alias='@type'
    )
