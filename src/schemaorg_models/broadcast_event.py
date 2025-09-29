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
from .publication_event import PublicationEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .language import Language
    from .event import Event

class BroadcastEvent(PublicationEvent):
    '''
    An over the air or online broadcast event.

    Attributes:
        videoFormat: The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).
        broadcastOfEvent: The event being broadcast such as a sporting event or awards ceremony.
        subtitleLanguage: Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).
        isLiveBroadcast: True if the broadcast is of a live event.
    '''
    class_: Literal['https://schema.org/BroadcastEvent'] = Field( # type: ignore
        default='https://schema.org/BroadcastEvent',
        alias='@type',
        serialization_alias='@type'
    )
    videoFormat: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    broadcastOfEvent: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    subtitleLanguage: Optional[Union['Language', List['Language'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    isLiveBroadcast: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
