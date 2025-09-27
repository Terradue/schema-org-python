from typing import List, Literal, Optional, Union
from datetime import datetime
from pydantic import AliasChoices, Field
from schemaorg_models.reservation import Reservation

from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.place import Place

class TaxiReservation(Reservation):
    """
A reservation for a taxi.\
\
Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
    class_: Literal['https://schema.org/TaxiReservation'] = Field(default='https://schema.org/TaxiReservation', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    partySize: Optional[Union[int, List[int], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('partySize', 'https://schema.org/partySize'), serialization_alias='https://schema.org/partySize')
    pickupLocation: Optional[Union[Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('pickupLocation', 'https://schema.org/pickupLocation'), serialization_alias='https://schema.org/pickupLocation')
    pickupTime: Optional[Union[datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('pickupTime', 'https://schema.org/pickupTime'), serialization_alias='https://schema.org/pickupTime')
