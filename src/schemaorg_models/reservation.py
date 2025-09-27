from typing import List, Literal, Optional, Union
from datetime import datetime
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization
from schemaorg_models.thing import Thing
from schemaorg_models.ticket import Ticket
from schemaorg_models.program_membership import ProgramMembership

class Reservation(Intangible):
    """
Describes a reservation for travel, dining or an event. Some reservations require tickets. \
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use [[Offer]].
    """
    class_: Literal['https://schema.org/Reservation'] = Field(default='https://schema.org/Reservation', alias='@type', serialization_alias='@type') # type: ignore
    reservationStatus: Optional[Union["ReservationStatusType", List["ReservationStatusType"]]] = Field(default=None, validation_alias=AliasChoices('reservationStatus', 'https://schema.org/reservationStatus'), serialization_alias='https://schema.org/reservationStatus')
    bookingAgent: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('bookingAgent', 'https://schema.org/bookingAgent'), serialization_alias='https://schema.org/bookingAgent')
    reservationFor: Optional[Union[Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('reservationFor', 'https://schema.org/reservationFor'), serialization_alias='https://schema.org/reservationFor')
    totalPrice: Optional[Union[str, List[str], "PriceSpecification", List["PriceSpecification"], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('totalPrice', 'https://schema.org/totalPrice'), serialization_alias='https://schema.org/totalPrice')
    priceCurrency: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('priceCurrency', 'https://schema.org/priceCurrency'), serialization_alias='https://schema.org/priceCurrency')
    broker: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('broker', 'https://schema.org/broker'), serialization_alias='https://schema.org/broker')
    bookingTime: Optional[Union[datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('bookingTime', 'https://schema.org/bookingTime'), serialization_alias='https://schema.org/bookingTime')
    provider: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('provider', 'https://schema.org/provider'), serialization_alias='https://schema.org/provider')
    reservationId: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('reservationId', 'https://schema.org/reservationId'), serialization_alias='https://schema.org/reservationId')
    underName: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('underName', 'https://schema.org/underName'), serialization_alias='https://schema.org/underName')
    reservedTicket: Optional[Union[Ticket, List[Ticket]]] = Field(default=None, validation_alias=AliasChoices('reservedTicket', 'https://schema.org/reservedTicket'), serialization_alias='https://schema.org/reservedTicket')
    modifiedTime: Optional[Union[datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('modifiedTime', 'https://schema.org/modifiedTime'), serialization_alias='https://schema.org/modifiedTime')
    programMembershipUsed: Optional[Union[ProgramMembership, List[ProgramMembership]]] = Field(default=None, validation_alias=AliasChoices('programMembershipUsed', 'https://schema.org/programMembershipUsed'), serialization_alias='https://schema.org/programMembershipUsed')
