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

class PaymentMethodType(Enumeration):
    '''
    The type of payment method, only for generic payment types, specific forms of payments, like card payment should be expressed using subclasses of PaymentMethod.
    '''
    class_: Literal['https://schema.org/PaymentMethodType'] = Field( # type: ignore
        default='https://schema.org/PaymentMethodType',
        alias='@type',
        serialization_alias='@type'
    )
