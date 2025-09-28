from __future__ import annotations
from datetime import (
    datetime
)
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
from .place import Place

class RentalCarReservation(Reservation):
    """
A reservation for a rental car.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """
    class_: Literal['https://schema.org/RentalCarReservation'] = Field( # type: ignore
        default='https://schema.org/RentalCarReservation',
        alias='@type',
        serialization_alias='@type'
    )
    pickupTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pickupTime',
            'https://schema.org/pickupTime'
        ),
        serialization_alias='https://schema.org/pickupTime'
    )
    dropoffTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dropoffTime',
            'https://schema.org/dropoffTime'
        ),
        serialization_alias='https://schema.org/dropoffTime'
    )
    dropoffLocation: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dropoffLocation',
            'https://schema.org/dropoffLocation'
        ),
        serialization_alias='https://schema.org/dropoffLocation'
    )
    pickupLocation: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pickupLocation',
            'https://schema.org/pickupLocation'
        ),
        serialization_alias='https://schema.org/pickupLocation'
    )
