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

class AdultEntertainment(EntertainmentBusiness):
    '''
    An adult entertainment establishment.
    '''
    class_: Literal['https://schema.org/AdultEntertainment'] = Field( # type: ignore
        default='https://schema.org/AdultEntertainment',
        alias='@type',
        serialization_alias='@type'
    )
