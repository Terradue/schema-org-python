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
from .performing_group import PerformingGroup
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .music_album import MusicAlbum
    from .music_recording import MusicRecording
    from .item_list import ItemList
    from .person import Person

class MusicGroup(PerformingGroup):
    """
A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.
    """
    class_: Literal['https://schema.org/MusicGroup'] = Field( # type: ignore
        default='https://schema.org/MusicGroup',
        alias='@type',
        serialization_alias='@type'
    )
    albums: Optional[Union["MusicAlbum", List["MusicAlbum"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albums',
            'https://schema.org/albums'
        ),
        serialization_alias='https://schema.org/albums'
    )
    album: Optional[Union["MusicAlbum", List["MusicAlbum"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'album',
            'https://schema.org/album'
        ),
        serialization_alias='https://schema.org/album'
    )
    musicGroupMember: Optional[Union["Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicGroupMember',
            'https://schema.org/musicGroupMember'
        ),
        serialization_alias='https://schema.org/musicGroupMember'
    )
    tracks: Optional[Union["MusicRecording", List["MusicRecording"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tracks',
            'https://schema.org/tracks'
        ),
        serialization_alias='https://schema.org/tracks'
    )
    track: Optional[Union["ItemList", List["ItemList"], "MusicRecording", List["MusicRecording"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'track',
            'https://schema.org/track'
        ),
        serialization_alias='https://schema.org/track'
    )
    genre: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
