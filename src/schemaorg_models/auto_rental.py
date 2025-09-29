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
from .automotive_business import AutomotiveBusiness

class AutoRental(AutomotiveBusiness):
    '''
    A car rental business.
    '''
    class_: Literal['https://schema.org/AutoRental'] = Field( # type: ignore
        default='https://schema.org/AutoRental',
        alias='@type',
        serialization_alias='@type'
    )
