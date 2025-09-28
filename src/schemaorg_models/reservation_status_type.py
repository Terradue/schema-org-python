from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .status_enumeration import StatusEnumeration

class ReservationStatusType(StatusEnumeration):
    """
Enumerated status values for Reservation.
    """
    class_: Literal['https://schema.org/ReservationStatusType'] = Field( # type: ignore
        default='https://schema.org/ReservationStatusType',
        alias='@type',
        serialization_alias='@type'
    )
