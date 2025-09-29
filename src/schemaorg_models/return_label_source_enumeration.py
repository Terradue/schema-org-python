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

class ReturnLabelSourceEnumeration(Enumeration):
    '''
    Enumerates several types of return labels for product returns.
    '''
    class_: Literal['https://schema.org/ReturnLabelSourceEnumeration'] = Field( # type: ignore
        default='https://schema.org/ReturnLabelSourceEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
