from typing import List, Literal, Optional, Union
from datetime import datetime
from pydantic import AliasChoices, Field
from schemaorg_models.trip import Trip

from schemaorg_models.boarding_policy_type import BoardingPolicyType
from schemaorg_models.airport import Airport
from schemaorg_models.organization import Organization
from schemaorg_models.person import Person
from schemaorg_models.vehicle import Vehicle

class Flight(Trip):
    """
An airline flight.
    """
    class_: Literal['https://schema.org/Flight'] = Field(default='https://schema.org/Flight', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    boardingPolicy: Optional[Union[BoardingPolicyType, List[BoardingPolicyType]]] = Field(default=None, validation_alias=AliasChoices('boardingPolicy', 'https://schema.org/boardingPolicy'), serialization_alias='https://schema.org/boardingPolicy')
    estimatedFlightDuration: Optional[Union[str, List[str], "Duration", List["Duration"]]] = Field(default=None, validation_alias=AliasChoices('estimatedFlightDuration', 'https://schema.org/estimatedFlightDuration'), serialization_alias='https://schema.org/estimatedFlightDuration')
    departureAirport: Optional[Union[Airport, List[Airport]]] = Field(default=None, validation_alias=AliasChoices('departureAirport', 'https://schema.org/departureAirport'), serialization_alias='https://schema.org/departureAirport')
    carrier: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('carrier', 'https://schema.org/carrier'), serialization_alias='https://schema.org/carrier')
    departureGate: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('departureGate', 'https://schema.org/departureGate'), serialization_alias='https://schema.org/departureGate')
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('seller', 'https://schema.org/seller'), serialization_alias='https://schema.org/seller')
    arrivalTerminal: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('arrivalTerminal', 'https://schema.org/arrivalTerminal'), serialization_alias='https://schema.org/arrivalTerminal')
    flightDistance: Optional[Union[str, List[str], "Distance", List["Distance"]]] = Field(default=None, validation_alias=AliasChoices('flightDistance', 'https://schema.org/flightDistance'), serialization_alias='https://schema.org/flightDistance')
    webCheckinTime: Optional[Union[datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('webCheckinTime', 'https://schema.org/webCheckinTime'), serialization_alias='https://schema.org/webCheckinTime')
    mealService: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('mealService', 'https://schema.org/mealService'), serialization_alias='https://schema.org/mealService')
    aircraft: Optional[Union[Vehicle, List[Vehicle], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('aircraft', 'https://schema.org/aircraft'), serialization_alias='https://schema.org/aircraft')
    arrivalGate: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('arrivalGate', 'https://schema.org/arrivalGate'), serialization_alias='https://schema.org/arrivalGate')
    flightNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('flightNumber', 'https://schema.org/flightNumber'), serialization_alias='https://schema.org/flightNumber')
    departureTerminal: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('departureTerminal', 'https://schema.org/departureTerminal'), serialization_alias='https://schema.org/departureTerminal')
    arrivalAirport: Optional[Union[Airport, List[Airport]]] = Field(default=None, validation_alias=AliasChoices('arrivalAirport', 'https://schema.org/arrivalAirport'), serialization_alias='https://schema.org/arrivalAirport')
