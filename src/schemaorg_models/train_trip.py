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
            'arrivalStation',
            'https://schema.org/arrivalStation'
        ),
        serialization_alias='https://schema.org/arrivalStation'
    )
    trainName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trainName',
            'https://schema.org/trainName'
        ),
        serialization_alias='https://schema.org/trainName'
    )
    departureStation: Optional[Union['TrainStation', List['TrainStation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departureStation',
            'https://schema.org/departureStation'
        ),
        serialization_alias='https://schema.org/departureStation'
    )
    departurePlatform: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departurePlatform',
            'https://schema.org/departurePlatform'
        ),
        serialization_alias='https://schema.org/departurePlatform'
    )
    arrivalPlatform: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'arrivalPlatform',
            'https://schema.org/arrivalPlatform'
        ),
        serialization_alias='https://schema.org/arrivalPlatform'
    )
    trainNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trainNumber',
            'https://schema.org/trainNumber'
        ),
        serialization_alias='https://schema.org/trainNumber'
    )
