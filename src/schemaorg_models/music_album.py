from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.music_playlist import MusicPlaylist

from schemaorg_models.person import Person
from schemaorg_models.music_album_production_type import MusicAlbumProductionType
from schemaorg_models.music_album_release_type import MusicAlbumReleaseType

class MusicAlbum(MusicPlaylist):
    """
A collection of music tracks.
    """
    type_: Literal['https://schema.org/MusicAlbum'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MusicAlbum'),serialization_alias='class') # type: ignore
    albumRelease: Optional[Union["MusicRelease", List["MusicRelease"]]] = Field(default=None,validation_alias=AliasChoices('albumRelease', 'https://schema.org/albumRelease'),serialization_alias='https://schema.org/albumRelease')
    byArtist: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('byArtist', 'https://schema.org/byArtist'),serialization_alias='https://schema.org/byArtist')
    albumProductionType: Optional[Union[MusicAlbumProductionType, List[MusicAlbumProductionType]]] = Field(default=None,validation_alias=AliasChoices('albumProductionType', 'https://schema.org/albumProductionType'),serialization_alias='https://schema.org/albumProductionType')
    albumReleaseType: Optional[Union[MusicAlbumReleaseType, List[MusicAlbumReleaseType]]] = Field(default=None,validation_alias=AliasChoices('albumReleaseType', 'https://schema.org/albumReleaseType'),serialization_alias='https://schema.org/albumReleaseType')
