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
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .qualitative_value import QualitativeValue

class FlightReservation(Reservation):
    '''
    A reservation for air travel.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].

    Attributes:
        boardingGroup: The airline-specific indicator of boarding order / preference.
        passengerPriorityStatus: The priority status assigned to a passenger for security or boarding (e.g. FastTrack or Priority).
        passengerSequenceNumber: The passenger's sequence number as assigned by the airline.
        securityScreening: The type of security screening the passenger is subject to.
    '''
    class_: Literal['https://schema.org/FlightReservation'] = Field( # type: ignore
        default='https://schema.org/FlightReservation',
        alias='@type',
        serialization_alias='@type'
    )
    boardingGroup: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    passengerPriorityStatus: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    passengerSequenceNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    securityScreening: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
