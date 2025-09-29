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
from .performing_group import PerformingGroup
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .item_list import ItemList
    from .person import Person
    from .music_recording import MusicRecording
    from .music_album import MusicAlbum

class MusicGroup(PerformingGroup):
    '''
    A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.

    Attributes:
        albums: A collection of music albums.
        album: A music album.
        musicGroupMember: A member of a music group&#x2014;for example, John, Paul, George, or Ringo.
        tracks: A music recording (track)&#x2014;usually a single song.
        track: A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.
        genre: Genre of the creative work, broadcast channel or group.
    '''
    class_: Literal['https://schema.org/MusicGroup'] = Field( # type: ignore
        default='https://schema.org/MusicGroup',
        alias='@type',
        serialization_alias='@type'
    )
    albums: Optional[Union['MusicAlbum', List['MusicAlbum']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    album: Optional[Union['MusicAlbum', List['MusicAlbum']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    musicGroupMember: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
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
    genre: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
