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
    from .quantitative_value import QuantitativeValue
    from .place import Place

class TaxiReservation(Reservation):
    '''
    A reservation for a taxi.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].

    Attributes:
        partySize: Number of people the reservation should accommodate.
        pickupLocation: Where a taxi will pick up a passenger or a rental car can be picked up.
        pickupTime: When a taxi will pick up a passenger or a rental car can be picked up.
    '''
    class_: Literal['https://schema.org/TaxiReservation'] = Field( # type: ignore
        default='https://schema.org/TaxiReservation',
        alias='@type',
        serialization_alias='@type'
    )
    partySize: Optional[Union[int, List[int], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partySize',
            'https://schema.org/partySize'
        ),
        serialization_alias='https://schema.org/partySize'
    )
    pickupLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pickupLocation',
            'https://schema.org/pickupLocation'
        ),
        serialization_alias='https://schema.org/pickupLocation'
    )
    pickupTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pickupTime',
            'https://schema.org/pickupTime'
        ),
        serialization_alias='https://schema.org/pickupTime'
    )
