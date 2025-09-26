from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.reservation import Reservation

from schemaorg_models.qualitative_value import QualitativeValue

class FlightReservation(Reservation):
    """
A reservation for air travel.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    boardingGroup: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('boardingGroup', 'https://schema.org/boardingGroup'),serialization_alias='https://schema.org/boardingGroup')
    passengerPriorityStatus: Optional[Union[str, List[str], QualitativeValue, List[QualitativeValue]]] = Field(default=None,validation_alias=AliasChoices('passengerPriorityStatus', 'https://schema.org/passengerPriorityStatus'),serialization_alias='https://schema.org/passengerPriorityStatus')
    passengerSequenceNumber: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('passengerSequenceNumber', 'https://schema.org/passengerSequenceNumber'),serialization_alias='https://schema.org/passengerSequenceNumber')
    securityScreening: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('securityScreening', 'https://schema.org/securityScreening'),serialization_alias='https://schema.org/securityScreening')
