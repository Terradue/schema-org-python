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

class ProductReturnEnumeration(Enumeration):
    '''
    ProductReturnEnumeration enumerates several kinds of product return policy. Note that this structure may not capture all aspects of the policy.
    '''
    class_: Literal['https://schema.org/ProductReturnEnumeration'] = Field( # type: ignore
        default='https://schema.org/ProductReturnEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
