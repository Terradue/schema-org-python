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
from .permit import Permit

class GovernmentPermit(Permit):
    '''
    A permit issued by a government agency.
    '''
    class_: Literal['https://schema.org/GovernmentPermit'] = Field( # type: ignore
        default='https://schema.org/GovernmentPermit',
        alias='@type',
        serialization_alias='@type'
    )
