from __future__ import annotations
from pydantic import (
    AliasChoices,
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
    from .cable_or_satellite_service import CableOrSatelliteService
    from .broadcast_service import BroadcastService

class BroadcastChannel(Intangible):
    """
A unique instance of a BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/BroadcastChannel'] = Field( # type: ignore
        default='https://schema.org/BroadcastChannel',
        alias='@type',
        serialization_alias='@type'
    )
    inBroadcastLineup: Optional[Union["CableOrSatelliteService", List["CableOrSatelliteService"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inBroadcastLineup',
            'https://schema.org/inBroadcastLineup'
        ),
        serialization_alias='https://schema.org/inBroadcastLineup'
    )
    broadcastChannelId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastChannelId',
            'https://schema.org/broadcastChannelId'
        ),
        serialization_alias='https://schema.org/broadcastChannelId'
    )
    providesBroadcastService: Optional[Union["BroadcastService", List["BroadcastService"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'providesBroadcastService',
            'https://schema.org/providesBroadcastService'
        ),
        serialization_alias='https://schema.org/providesBroadcastService'
    )
    broadcastFrequency: Optional[Union[str, List[str], "BroadcastFrequencySpecification", List["BroadcastFrequencySpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastFrequency',
            'https://schema.org/broadcastFrequency'
        ),
        serialization_alias='https://schema.org/broadcastFrequency'
    )
    broadcastServiceTier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastServiceTier',
            'https://schema.org/broadcastServiceTier'
        ),
        serialization_alias='https://schema.org/broadcastServiceTier'
    )
    genre: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
