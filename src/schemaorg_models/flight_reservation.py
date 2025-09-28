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
from .qualitative_value import QualitativeValue
from .reservation import Reservation

class FlightReservation(Reservation):
    """
A reservation for air travel.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    class_: Literal['https://schema.org/FlightReservation'] = Field( # type: ignore
        default='https://schema.org/FlightReservation',
        alias='@type',
        serialization_alias='@type'
    )
    boardingGroup: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'boardingGroup',
            'https://schema.org/boardingGroup'
        ),
        serialization_alias='https://schema.org/boardingGroup'
    )
    passengerPriorityStatus: Optional[Union[str, List[str], QualitativeValue, List[QualitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'passengerPriorityStatus',
            'https://schema.org/passengerPriorityStatus'
        ),
        serialization_alias='https://schema.org/passengerPriorityStatus'
    )
    passengerSequenceNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'passengerSequenceNumber',
            'https://schema.org/passengerSequenceNumber'
        ),
        serialization_alias='https://schema.org/passengerSequenceNumber'
    )
    securityScreening: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'securityScreening',
            'https://schema.org/securityScreening'
        ),
        serialization_alias='https://schema.org/securityScreening'
    )
