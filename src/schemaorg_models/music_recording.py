from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.music_playlist import MusicPlaylist
from schemaorg_models.music_composition import MusicComposition
from schemaorg_models.person import Person

class MusicRecording(CreativeWork):
    """
A music recording (track), usually a single song.
    """
    inPlaylist: Optional[Union[MusicPlaylist, List[MusicPlaylist]]] = Field(default=None,validation_alias=AliasChoices('inPlaylist', 'https://schema.org/inPlaylist'),serialization_alias='https://schema.org/inPlaylist')
    inAlbum: Optional[Union["MusicAlbum", List["MusicAlbum"]]] = Field(default=None,validation_alias=AliasChoices('inAlbum', 'https://schema.org/inAlbum'),serialization_alias='https://schema.org/inAlbum')
    recordingOf: Optional[Union[MusicComposition, List[MusicComposition]]] = Field(default=None,validation_alias=AliasChoices('recordingOf', 'https://schema.org/recordingOf'),serialization_alias='https://schema.org/recordingOf')
    byArtist: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('byArtist', 'https://schema.org/byArtist'),serialization_alias='https://schema.org/byArtist')
    isrcCode: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('isrcCode', 'https://schema.org/isrcCode'),serialization_alias='https://schema.org/isrcCode')
    duration: Optional[Union["Duration", List["Duration"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('duration', 'https://schema.org/duration'),serialization_alias='https://schema.org/duration')
