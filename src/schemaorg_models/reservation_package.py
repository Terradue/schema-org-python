from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .reservation import Reservation

class ReservationPackage(Reservation):
    """
A group of multiple reservations with common values for all sub-reservations.
    """
    class_: Literal['https://schema.org/ReservationPackage'] = Field( # type: ignore
        default='https://schema.org/ReservationPackage',
        alias='@type',
        serialization_alias='@type'
    )
    subReservation: Optional[Union[Reservation, List[Reservation]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subReservation',
            'https://schema.org/subReservation'
        ),
        serialization_alias='https://schema.org/subReservation'
    )
