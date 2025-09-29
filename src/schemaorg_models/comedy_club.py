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

class ComedyClub(EntertainmentBusiness):
    '''
    A comedy club.
    '''
    class_: Literal['https://schema.org/ComedyClub'] = Field( # type: ignore
        default='https://schema.org/ComedyClub',
        alias='@type',
        serialization_alias='@type'
    )
