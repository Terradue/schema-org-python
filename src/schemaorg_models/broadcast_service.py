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
from .service import Service
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .place import Place
    from .language import Language
    from .broadcast_frequency_specification import BroadcastFrequencySpecification
    from .organization import Organization
    from .broadcast_channel import BroadcastChannel

class BroadcastService(Service):
    '''
    A delivery service through which content is provided via broadcast over the air or online.

    Attributes:
        callSign: A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.
        broadcastAffiliateOf: The media network(s) whose content is broadcast on this station.
        broadcaster: The organization owning or operating the broadcast service.
        area: The area within which users can expect to reach the broadcast service.
        videoFormat: The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).
        broadcastDisplayName: The name displayed in the channel guide. For many US affiliates, it is the network name.
        inLanguage: The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        broadcastFrequency: The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g. 87-99. In addition a shortcut idiom is supported for frequencies of AM and FM radio channels, e.g. "87 FM".
        hasBroadcastChannel: A broadcast channel of a broadcast service.
        parentService: A broadcast service to which the broadcast service may belong to such as regional variations of a national channel.
        broadcastTimezone: The timezone in [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601) for which the service bases its broadcasts.
    '''
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
    broadcastAffiliateOf: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastAffiliateOf',
            'https://schema.org/broadcastAffiliateOf'
        ),
        serialization_alias='https://schema.org/broadcastAffiliateOf'
    )
    broadcaster: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcaster',
            'https://schema.org/broadcaster'
        ),
        serialization_alias='https://schema.org/broadcaster'
    )
    area: Optional[Union['Place', List['Place']]] = Field(
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
    inLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
    broadcastFrequency: Optional[Union[str, List[str], 'BroadcastFrequencySpecification', List['BroadcastFrequencySpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastFrequency',
            'https://schema.org/broadcastFrequency'
        ),
        serialization_alias='https://schema.org/broadcastFrequency'
    )
    hasBroadcastChannel: Optional[Union['BroadcastChannel', List['BroadcastChannel']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasBroadcastChannel',
            'https://schema.org/hasBroadcastChannel'
        ),
        serialization_alias='https://schema.org/hasBroadcastChannel'
    )
    parentService: Optional[Union['BroadcastService', List['BroadcastService']]] = Field(
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
