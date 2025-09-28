from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

from datetime import (
    date,
    datetime
)
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.person import Person
from schemaorg_models.organization import Organization

class Ticket(Intangible):
    """
Used to describe a ticket to an event, a flight, a bus ride, etc.
    """
    class_: Literal['https://schema.org/Ticket'] = Field( # type: ignore
        default='https://schema.org/Ticket',
        alias='@type',
        serialization_alias='@type'
    )
    underName: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(
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
    ticketedSeat: Optional[Union["Seat", List["Seat"]]] = Field(
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
    totalPrice: Optional[Union[str, List[str], "PriceSpecification", List["PriceSpecification"], float, List[float]]] = Field(
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
    issuedBy: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issuedBy',
            'https://schema.org/issuedBy'
        ),
        serialization_alias='https://schema.org/issuedBy'
    )
