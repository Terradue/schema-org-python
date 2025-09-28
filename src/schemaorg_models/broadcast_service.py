from __future__ import annotations
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
from .service import Service
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .broadcast_frequency_specification import BroadcastFrequencySpecification
    from .organization import Organization
    from .broadcast_channel import BroadcastChannel
    from .language import Language
    from .place import Place

class BroadcastService(Service):
    """
A delivery service through which content is provided via broadcast over the air or online.
    """
    class_: Literal['https://schema.org/BroadcastService'] = Field( # type: ignore
        default='https://schema.org/BroadcastService',
        alias='@type',
        serialization_alias='@type'
    )
    callSign: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'callSign',
            'https://schema.org/callSign'
        ),
        serialization_alias='https://schema.org/callSign'
    )
    broadcastAffiliateOf: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastAffiliateOf',
            'https://schema.org/broadcastAffiliateOf'
        ),
        serialization_alias='https://schema.org/broadcastAffiliateOf'
    )
    broadcaster: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcaster',
            'https://schema.org/broadcaster'
        ),
        serialization_alias='https://schema.org/broadcaster'
    )
    area: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'area',
            'https://schema.org/area'
        ),
        serialization_alias='https://schema.org/area'
    )
    videoFormat: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'videoFormat',
            'https://schema.org/videoFormat'
        ),
        serialization_alias='https://schema.org/videoFormat'
    )
    broadcastDisplayName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastDisplayName',
            'https://schema.org/broadcastDisplayName'
        ),
        serialization_alias='https://schema.org/broadcastDisplayName'
    )
    inLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
    broadcastFrequency: Optional[Union[str, List[str], "BroadcastFrequencySpecification", List["BroadcastFrequencySpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastFrequency',
            'https://schema.org/broadcastFrequency'
        ),
        serialization_alias='https://schema.org/broadcastFrequency'
    )
    hasBroadcastChannel: Optional[Union["BroadcastChannel", List["BroadcastChannel"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasBroadcastChannel',
            'https://schema.org/hasBroadcastChannel'
        ),
        serialization_alias='https://schema.org/hasBroadcastChannel'
    )
    parentService: Optional[Union["BroadcastService", List["BroadcastService"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parentService',
            'https://schema.org/parentService'
        ),
        serialization_alias='https://schema.org/parentService'
    )
    broadcastTimezone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastTimezone',
            'https://schema.org/broadcastTimezone'
        ),
        serialization_alias='https://schema.org/broadcastTimezone'
    )
