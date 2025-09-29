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
from .enumeration import Enumeration

class ItemAvailability(Enumeration):
    '''
    A list of possible product availability options.
    '''
    class_: Literal['https://schema.org/ItemAvailability'] = Field( # type: ignore
        default='https://schema.org/ItemAvailability',
        alias='@type',
        serialization_alias='@type'
    )
