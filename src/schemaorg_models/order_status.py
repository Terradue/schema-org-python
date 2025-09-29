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
from .status_enumeration import StatusEnumeration

class OrderStatus(StatusEnumeration):
    '''
    Enumerated status values for Order.
    '''
    class_: Literal['https://schema.org/OrderStatus'] = Field( # type: ignore
        default='https://schema.org/OrderStatus',
        alias='@type',
        serialization_alias='@type'
    )
