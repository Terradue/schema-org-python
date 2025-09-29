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
    from .music_recording import MusicRecording
    from .item_list import ItemList

class MusicPlaylist(CreativeWork):
    '''
    A collection of music tracks in playlist form.

    Attributes:
        tracks: A music recording (track)&#x2014;usually a single song.
        track: A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.
        numTracks: The number of tracks in this album or playlist.
    '''
    class_: Literal['https://schema.org/MusicPlaylist'] = Field( # type: ignore
        default='https://schema.org/MusicPlaylist',
        alias='@type',
        serialization_alias='@type'
    )
    tracks: Optional[Union['MusicRecording', List['MusicRecording']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    track: Optional[Union['ItemList', List['ItemList'], 'MusicRecording', List['MusicRecording']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    numTracks: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
