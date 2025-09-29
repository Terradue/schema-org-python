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

class OfferItemCondition(Enumeration):
    '''
    A list of possible conditions for the item.
    '''
    class_: Literal['https://schema.org/OfferItemCondition'] = Field( # type: ignore
        default='https://schema.org/OfferItemCondition',
        alias='@type',
        serialization_alias='@type'
    )
