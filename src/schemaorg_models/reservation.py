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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .program_membership import ProgramMembership
    from .price_specification import PriceSpecification
    from .ticket import Ticket
    from .thing import Thing
    from .reservation_status_type import ReservationStatusType
    from .person import Person
    from .organization import Organization

class Reservation(Intangible):
    '''
    Describes a reservation for travel, dining or an event. Some reservations require tickets. \
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use [[Offer]].

    Attributes:
        reservationStatus: The current status of the reservation.
        bookingAgent: 'bookingAgent' is an out-dated term indicating a 'broker' that serves as a booking agent.
        reservationFor: The thing -- flight, event, restaurant, etc. being reserved.
        totalPrice: The total price for the reservation or ticket, including applicable taxes, shipping, etc.\
\
Usage guidelines:\
\
* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\
* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        priceCurrency: The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        broker: An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.
        bookingTime: The date and time the reservation was booked.
        provider: The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        reservationId: A unique identifier for the reservation.
        underName: The person or organization the reservation or ticket is for.
        reservedTicket: A ticket associated with the reservation.
        modifiedTime: The date and time the reservation was modified.
        programMembershipUsed: Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the reservation.
    '''
    class_: Literal['https://schema.org/Reservation'] = Field( # type: ignore
        default='https://schema.org/Reservation',
        alias='@type',
        serialization_alias='@type'
    )
    reservationStatus: Optional[Union['ReservationStatusType', List['ReservationStatusType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reservationStatus',
            'https://schema.org/reservationStatus'
        ),
        serialization_alias='https://schema.org/reservationStatus'
    )
    bookingAgent: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bookingAgent',
            'https://schema.org/bookingAgent'
        ),
        serialization_alias='https://schema.org/bookingAgent'
    )
    reservationFor: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reservationFor',
            'https://schema.org/reservationFor'
        ),
        serialization_alias='https://schema.org/reservationFor'
    )
    totalPrice: Optional[Union[str, List[str], 'PriceSpecification', List['PriceSpecification'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'totalPrice',
            'https://schema.org/totalPrice'
        ),
        serialization_alias='https://schema.org/totalPrice'
    )
    priceCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceCurrency',
            'https://schema.org/priceCurrency'
        ),
        serialization_alias='https://schema.org/priceCurrency'
    )
    broker: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broker',
            'https://schema.org/broker'
        ),
        serialization_alias='https://schema.org/broker'
    )
    bookingTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bookingTime',
            'https://schema.org/bookingTime'
        ),
        serialization_alias='https://schema.org/bookingTime'
    )
    provider: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    reservationId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reservationId',
            'https://schema.org/reservationId'
        ),
        serialization_alias='https://schema.org/reservationId'
    )
    underName: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'underName',
            'https://schema.org/underName'
        ),
        serialization_alias='https://schema.org/underName'
    )
    reservedTicket: Optional[Union['Ticket', List['Ticket']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reservedTicket',
            'https://schema.org/reservedTicket'
        ),
        serialization_alias='https://schema.org/reservedTicket'
    )
    modifiedTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'modifiedTime',
            'https://schema.org/modifiedTime'
        ),
        serialization_alias='https://schema.org/modifiedTime'
    )
    programMembershipUsed: Optional[Union['ProgramMembership', List['ProgramMembership']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'programMembershipUsed',
            'https://schema.org/programMembershipUsed'
        ),
        serialization_alias='https://schema.org/programMembershipUsed'
    )
