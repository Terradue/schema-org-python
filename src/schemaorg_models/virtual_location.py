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
from .intangible import Intangible

class VirtualLocation(Intangible):
    '''
    An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world.
    '''
    class_: Literal['https://schema.org/VirtualLocation'] = Field( # type: ignore
        default='https://schema.org/VirtualLocation',
        alias='@type',
        serialization_alias='@type'
    )
