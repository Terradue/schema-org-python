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
    from .train_station import TrainStation

class TrainTrip(Trip):
    '''
    A trip on a commercial train line.

    Attributes:
        arrivalStation: The station where the train trip ends.
        trainName: The name of the train (e.g. The Orient Express).
        departureStation: The station from which the train departs.
        departurePlatform: The platform from which the train departs.
        arrivalPlatform: The platform where the train arrives.
        trainNumber: The unique identifier for the train.
    '''
    class_: Literal['https://schema.org/TrainTrip'] = Field( # type: ignore
        default='https://schema.org/TrainTrip',
        alias='@type',
        serialization_alias='@type'
    )
    arrivalStation: Optional[Union['TrainStation', List['TrainStation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    trainName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    departureStation: Optional[Union['TrainStation', List['TrainStation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    departurePlatform: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    arrivalPlatform: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    trainNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
