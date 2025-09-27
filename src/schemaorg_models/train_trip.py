from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.trip import Trip

from schemaorg_models.train_station import TrainStation

class TrainTrip(Trip):
    """
A trip on a commercial train line.
    """
    type_: Literal['https://schema.org/TrainTrip'] = Field(default='https://schema.org/TrainTrip', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    arrivalStation: Optional[Union[TrainStation, List[TrainStation]]] = Field(default=None, validation_alias=AliasChoices('arrivalStation', 'https://schema.org/arrivalStation'), serialization_alias='https://schema.org/arrivalStation')
    trainName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('trainName', 'https://schema.org/trainName'), serialization_alias='https://schema.org/trainName')
    departureStation: Optional[Union[TrainStation, List[TrainStation]]] = Field(default=None, validation_alias=AliasChoices('departureStation', 'https://schema.org/departureStation'), serialization_alias='https://schema.org/departureStation')
    departurePlatform: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('departurePlatform', 'https://schema.org/departurePlatform'), serialization_alias='https://schema.org/departurePlatform')
    arrivalPlatform: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('arrivalPlatform', 'https://schema.org/arrivalPlatform'), serialization_alias='https://schema.org/arrivalPlatform')
    trainNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('trainNumber', 'https://schema.org/trainNumber'), serialization_alias='https://schema.org/trainNumber')
