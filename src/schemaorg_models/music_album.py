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
from .music_playlist import MusicPlaylist
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .music_album_release_type import MusicAlbumReleaseType
    from .music_group import MusicGroup
    from .music_album_production_type import MusicAlbumProductionType
    from .person import Person
    from .music_release import MusicRelease

class MusicAlbum(MusicPlaylist):
    """
A collection of music tracks.
    """
    class_: Literal['https://schema.org/MusicAlbum'] = Field( # type: ignore
        default='https://schema.org/MusicAlbum',
        alias='@type',
        serialization_alias='@type'
    )
    albumRelease: Optional[Union["MusicRelease", List["MusicRelease"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albumRelease',
            'https://schema.org/albumRelease'
        ),
        serialization_alias='https://schema.org/albumRelease'
    )
    byArtist: Optional[Union["MusicGroup", List["MusicGroup"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'byArtist',
            'https://schema.org/byArtist'
        ),
        serialization_alias='https://schema.org/byArtist'
    )
    albumProductionType: Optional[Union["MusicAlbumProductionType", List["MusicAlbumProductionType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albumProductionType',
            'https://schema.org/albumProductionType'
        ),
        serialization_alias='https://schema.org/albumProductionType'
    )
    albumReleaseType: Optional[Union["MusicAlbumReleaseType", List["MusicAlbumReleaseType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albumReleaseType',
            'https://schema.org/albumReleaseType'
        ),
        serialization_alias='https://schema.org/albumReleaseType'
    )
