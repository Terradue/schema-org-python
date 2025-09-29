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

class PaymentStatusType(StatusEnumeration):
    '''
    A specific payment status. For example, PaymentDue, PaymentComplete, etc.
    '''
    class_: Literal['https://schema.org/PaymentStatusType'] = Field( # type: ignore
        default='https://schema.org/PaymentStatusType',
        alias='@type',
        serialization_alias='@type'
    )
