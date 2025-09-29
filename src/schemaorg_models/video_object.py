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
from .media_object import MediaObject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .performing_group import PerformingGroup
    from .music_group import MusicGroup

class VideoObject(MediaObject):
    '''
    A video file.

    Attributes:
        directors: A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        videoFrameSize: The frame size of the video.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        transcript: If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
        actors: An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        videoQuality: The quality of the video.
        musicBy: The composer of the soundtrack.
        caption: The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        embeddedTextCaption: Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
    '''
    class_: Literal['https://schema.org/VideoObject'] = Field( # type: ignore
        default='https://schema.org/VideoObject',
        alias='@type',
        serialization_alias='@type'
    )
    directors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'directors',
            'https://schema.org/directors'
        ),
        serialization_alias='https://schema.org/directors'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    videoFrameSize: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'videoFrameSize',
            'https://schema.org/videoFrameSize'
        ),
        serialization_alias='https://schema.org/videoFrameSize'
    )
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    transcript: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transcript',
            'https://schema.org/transcript'
        ),
        serialization_alias='https://schema.org/transcript'
    )
    actors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
    )
    videoQuality: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'videoQuality',
            'https://schema.org/videoQuality'
        ),
        serialization_alias='https://schema.org/videoQuality'
    )
    musicBy: Optional[Union['MusicGroup', List['MusicGroup'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicBy',
            'https://schema.org/musicBy'
        ),
        serialization_alias='https://schema.org/musicBy'
    )
    caption: Optional[Union['MediaObject', List['MediaObject'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'caption',
            'https://schema.org/caption'
        ),
        serialization_alias='https://schema.org/caption'
    )
    embeddedTextCaption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'embeddedTextCaption',
            'https://schema.org/embeddedTextCaption'
        ),
        serialization_alias='https://schema.org/embeddedTextCaption'
    )
