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

class ReservationPackage(Reservation):
    '''
    A group of multiple reservations with common values for all sub-reservations.

    Attributes:
        subReservation: The individual reservations included in the package. Typically a repeated property.
    '''
    class_: Literal['https://schema.org/ReservationPackage'] = Field( # type: ignore
        default='https://schema.org/ReservationPackage',
        alias='@type',
        serialization_alias='@type'
    )
    subReservation: Optional[Union['Reservation', List['Reservation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subReservation',
            'https://schema.org/subReservation'
        ),
        serialization_alias='https://schema.org/subReservation'
    )
