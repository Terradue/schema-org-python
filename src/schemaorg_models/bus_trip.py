from __future__ import annotations

from .trip import Trip    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.bus_station import BusStation
from schemaorg_models.bus_stop import BusStop

class BusTrip(Trip):
    """
A trip on a commercial bus line.
    """
    class_: Literal['https://schema.org/BusTrip'] = Field( # type: ignore
        default='https://schema.org/BusTrip',
        alias='@type',
        serialization_alias='@type'
    )
    busNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'busNumber',
            'https://schema.org/busNumber'
        ),
        serialization_alias='https://schema.org/busNumber'
    )
    arrivalBusStop: Optional[Union[BusStation, List[BusStation], BusStop, List[BusStop]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'arrivalBusStop',
            'https://schema.org/arrivalBusStop'
        ),
        serialization_alias='https://schema.org/arrivalBusStop'
    )
    departureBusStop: Optional[Union[BusStop, List[BusStop], BusStation, List[BusStation]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departureBusStop',
            'https://schema.org/departureBusStop'
        ),
        serialization_alias='https://schema.org/departureBusStop'
    )
    busName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'busName',
            'https://schema.org/busName'
        ),
        serialization_alias='https://schema.org/busName'
    )
