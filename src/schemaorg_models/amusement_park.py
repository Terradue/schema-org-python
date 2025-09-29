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
from .entertainment_business import EntertainmentBusiness

class AmusementPark(EntertainmentBusiness):
    '''
    An amusement park.
    '''
    class_: Literal['https://schema.org/AmusementPark'] = Field( # type: ignore
        default='https://schema.org/AmusementPark',
        alias='@type',
        serialization_alias='@type'
    )
