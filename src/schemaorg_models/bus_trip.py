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
from .trip import Trip
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .bus_stop import BusStop
    from .bus_station import BusStation

class BusTrip(Trip):
    '''
    A trip on a commercial bus line.

    Attributes:
        busNumber: The unique identifier for the bus.
        arrivalBusStop: The stop or station from which the bus arrives.
        departureBusStop: The stop or station from which the bus departs.
        busName: The name of the bus (e.g. Bolt Express).
    '''
    class_: Literal['https://schema.org/BusTrip'] = Field( # type: ignore
        default='https://schema.org/BusTrip',
        alias='@type',
        serialization_alias='@type'
    )
    busNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    arrivalBusStop: Optional[Union['BusStation', List['BusStation'], 'BusStop', List['BusStop']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    departureBusStop: Optional[Union['BusStop', List['BusStop'], 'BusStation', List['BusStation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    busName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
