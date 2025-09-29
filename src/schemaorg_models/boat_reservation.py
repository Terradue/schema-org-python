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
from .reservation import Reservation

class BoatReservation(Reservation):
    '''
    A reservation for boat travel.

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    '''
    class_: Literal['https://schema.org/BoatReservation'] = Field( # type: ignore
        default='https://schema.org/BoatReservation',
        alias='@type',
        serialization_alias='@type'
    )
