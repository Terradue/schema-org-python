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
from .event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .language import Language
    from .movie import Movie

class ScreeningEvent(Event):
    '''
    A screening of a movie or other video.

    Attributes:
        subtitleLanguage: Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).
        videoFormat: The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).
        workPresented: The movie presented during this event.
    '''
    class_: Literal['https://schema.org/ScreeningEvent'] = Field( # type: ignore
        default='https://schema.org/ScreeningEvent',
        alias='@type',
        serialization_alias='@type'
    )
    subtitleLanguage: Optional[Union['Language', List['Language'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subtitleLanguage',
            'https://schema.org/subtitleLanguage'
        ),
        serialization_alias='https://schema.org/subtitleLanguage'
    )
    videoFormat: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'videoFormat',
            'https://schema.org/videoFormat'
        ),
        serialization_alias='https://schema.org/videoFormat'
    )
    workPresented: Optional[Union['Movie', List['Movie']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workPresented',
            'https://schema.org/workPresented'
        ),
        serialization_alias='https://schema.org/workPresented'
    )
