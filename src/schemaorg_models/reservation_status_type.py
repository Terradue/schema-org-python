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

class ReservationStatusType(StatusEnumeration):
    '''
    Enumerated status values for Reservation.
    '''
    class_: Literal['https://schema.org/ReservationStatusType'] = Field( # type: ignore
        default='https://schema.org/ReservationStatusType',
        alias='@type',
        serialization_alias='@type'
    )
