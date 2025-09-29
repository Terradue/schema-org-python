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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .duration import Duration
    from .music_playlist import MusicPlaylist
    from .music_composition import MusicComposition
    from .music_album import MusicAlbum
    from .music_group import MusicGroup
    from .person import Person
    from .quantitative_value import QuantitativeValue

class MusicRecording(CreativeWork):
    '''
    A music recording (track), usually a single song.

    Attributes:
        inPlaylist: The playlist to which this recording belongs.
        inAlbum: The album to which this recording belongs.
        recordingOf: The composition this track is a recording of.
        byArtist: The artist that performed this album or recording.
        isrcCode: The International Standard Recording Code for the recording.
        duration: The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
    '''
    class_: Literal['https://schema.org/MusicRecording'] = Field( # type: ignore
        default='https://schema.org/MusicRecording',
        alias='@type',
        serialization_alias='@type'
    )
    inPlaylist: Optional[Union['MusicPlaylist', List['MusicPlaylist']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inPlaylist',
            'https://schema.org/inPlaylist'
        ),
        serialization_alias='https://schema.org/inPlaylist'
    )
    inAlbum: Optional[Union['MusicAlbum', List['MusicAlbum']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inAlbum',
            'https://schema.org/inAlbum'
        ),
        serialization_alias='https://schema.org/inAlbum'
    )
    recordingOf: Optional[Union['MusicComposition', List['MusicComposition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recordingOf',
            'https://schema.org/recordingOf'
        ),
        serialization_alias='https://schema.org/recordingOf'
    )
    byArtist: Optional[Union['MusicGroup', List['MusicGroup'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'byArtist',
            'https://schema.org/byArtist'
        ),
        serialization_alias='https://schema.org/byArtist'
    )
    isrcCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isrcCode',
            'https://schema.org/isrcCode'
        ),
        serialization_alias='https://schema.org/isrcCode'
    )
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
