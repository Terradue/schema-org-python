from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.music_playlist import MusicPlaylist

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
from schemaorg_models.person import Person
from schemaorg_models.music_album_production_type import MusicAlbumProductionType
from schemaorg_models.music_album_release_type import MusicAlbumReleaseType

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
    byArtist: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'byArtist',
            'https://schema.org/byArtist'
        ),
        serialization_alias='https://schema.org/byArtist'
    )
    albumProductionType: Optional[Union[MusicAlbumProductionType, List[MusicAlbumProductionType]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albumProductionType',
            'https://schema.org/albumProductionType'
        ),
        serialization_alias='https://schema.org/albumProductionType'
    )
    albumReleaseType: Optional[Union[MusicAlbumReleaseType, List[MusicAlbumReleaseType]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albumReleaseType',
            'https://schema.org/albumReleaseType'
        ),
        serialization_alias='https://schema.org/albumReleaseType'
    )
