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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .broadcast_frequency_specification import BroadcastFrequencySpecification
    from .broadcast_service import BroadcastService
    from .cable_or_satellite_service import CableOrSatelliteService

class BroadcastChannel(Intangible):
    '''
    A unique instance of a BroadcastService on a CableOrSatelliteService lineup.

    Attributes:
        inBroadcastLineup: The CableOrSatelliteService offering the channel.
        broadcastChannelId: The unique address by which the BroadcastService can be identified in a provider lineup. In US, this is typically a number.
        providesBroadcastService: The BroadcastService offered on this channel.
        broadcastFrequency: The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g. 87-99. In addition a shortcut idiom is supported for frequencies of AM and FM radio channels, e.g. "87 FM".
        broadcastServiceTier: The type of service required to have access to the channel (e.g. Standard or Premium).
        genre: Genre of the creative work, broadcast channel or group.
    '''
    class_: Literal['https://schema.org/BroadcastChannel'] = Field( # type: ignore
        default='https://schema.org/BroadcastChannel',
        alias='@type',
        serialization_alias='@type'
    )
    inBroadcastLineup: Optional[Union['CableOrSatelliteService', List['CableOrSatelliteService']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    broadcastChannelId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    providesBroadcastService: Optional[Union['BroadcastService', List['BroadcastService']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    broadcastFrequency: Optional[Union[str, List[str], 'BroadcastFrequencySpecification', List['BroadcastFrequencySpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    broadcastServiceTier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    genre: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
