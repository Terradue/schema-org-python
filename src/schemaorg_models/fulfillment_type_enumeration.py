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

class FulfillmentTypeEnumeration(Enumeration):
    '''
    A type of product fulfillment.
    '''
    class_: Literal['https://schema.org/FulfillmentTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/FulfillmentTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
