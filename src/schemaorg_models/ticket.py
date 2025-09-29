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
    from .person import Person
    from .organization import Organization
    from .price_specification import PriceSpecification
    from .seat import Seat

class Ticket(Intangible):
    '''
    Used to describe a ticket to an event, a flight, a bus ride, etc.

    Attributes:
        underName: The person or organization the reservation or ticket is for.
        priceCurrency: The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        ticketedSeat: The seat associated with the ticket.
        dateIssued: The date the ticket was issued.
        ticketNumber: The unique identifier for the ticket.
        totalPrice: The total price for the reservation or ticket, including applicable taxes, shipping, etc.\
\
Usage guidelines:\
\
* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\
* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        ticketToken: Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.
        issuedBy: The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].
    '''
    class_: Literal['https://schema.org/Ticket'] = Field( # type: ignore
        default='https://schema.org/Ticket',
        alias='@type',
        serialization_alias='@type'
    )
    underName: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'underName',
            'https://schema.org/underName'
        ),
        serialization_alias='https://schema.org/underName'
    )
    priceCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceCurrency',
            'https://schema.org/priceCurrency'
        ),
        serialization_alias='https://schema.org/priceCurrency'
    )
    ticketedSeat: Optional[Union['Seat', List['Seat']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ticketedSeat',
            'https://schema.org/ticketedSeat'
        ),
        serialization_alias='https://schema.org/ticketedSeat'
    )
    dateIssued: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateIssued',
            'https://schema.org/dateIssued'
        ),
        serialization_alias='https://schema.org/dateIssued'
    )
    ticketNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ticketNumber',
            'https://schema.org/ticketNumber'
        ),
        serialization_alias='https://schema.org/ticketNumber'
    )
    totalPrice: Optional[Union[str, List[str], 'PriceSpecification', List['PriceSpecification'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'totalPrice',
            'https://schema.org/totalPrice'
        ),
        serialization_alias='https://schema.org/totalPrice'
    )
    ticketToken: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ticketToken',
            'https://schema.org/ticketToken'
        ),
        serialization_alias='https://schema.org/ticketToken'
    )
    issuedBy: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issuedBy',
            'https://schema.org/issuedBy'
        ),
        serialization_alias='https://schema.org/issuedBy'
    )
