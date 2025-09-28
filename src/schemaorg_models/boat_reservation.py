from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .reservation import Reservation

class BoatReservation(Reservation):
    """
A reservation for boat travel.

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    class_: Literal['https://schema.org/BoatReservation'] = Field( # type: ignore
        default='https://schema.org/BoatReservation',
        alias='@type',
        serialization_alias='@type'
    )
