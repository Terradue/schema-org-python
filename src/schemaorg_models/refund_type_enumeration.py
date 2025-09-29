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

class RefundTypeEnumeration(Enumeration):
    '''
    Enumerates several kinds of product return refund types.
    '''
    class_: Literal['https://schema.org/RefundTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/RefundTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
