from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization

class Ticket(Intangible):
    """
Used to describe a ticket to an event, a flight, a bus ride, etc.
    """
    class_: Literal['https://schema.org/Ticket'] = Field(default='https://schema.org/Ticket', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    underName: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('underName', 'https://schema.org/underName'), serialization_alias='https://schema.org/underName')
    priceCurrency: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('priceCurrency', 'https://schema.org/priceCurrency'), serialization_alias='https://schema.org/priceCurrency')
    ticketedSeat: Optional[Union["Seat", List["Seat"]]] = Field(default=None, validation_alias=AliasChoices('ticketedSeat', 'https://schema.org/ticketedSeat'), serialization_alias='https://schema.org/ticketedSeat')
    dateIssued: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('dateIssued', 'https://schema.org/dateIssued'), serialization_alias='https://schema.org/dateIssued')
    ticketNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('ticketNumber', 'https://schema.org/ticketNumber'), serialization_alias='https://schema.org/ticketNumber')
    totalPrice: Optional[Union[str, List[str], "PriceSpecification", List["PriceSpecification"], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('totalPrice', 'https://schema.org/totalPrice'), serialization_alias='https://schema.org/totalPrice')
    ticketToken: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('ticketToken', 'https://schema.org/ticketToken'), serialization_alias='https://schema.org/ticketToken')
    @field_serializer('ticketToken')
    def ticketToken2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    issuedBy: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('issuedBy', 'https://schema.org/issuedBy'), serialization_alias='https://schema.org/issuedBy')
