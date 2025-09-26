from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.item_list import ItemList

class MusicPlaylist(CreativeWork):
    """
A collection of music tracks in playlist form.
    """
    tracks: Optional[Union["MusicRecording", List["MusicRecording"]]] = Field(default=None,validation_alias=AliasChoices('tracks', 'https://schema.org/tracks'),serialization_alias='https://schema.org/tracks')
    track: Optional[Union[ItemList, List[ItemList], "MusicRecording", List["MusicRecording"]]] = Field(default=None,validation_alias=AliasChoices('track', 'https://schema.org/track'),serialization_alias='https://schema.org/track')
    numTracks: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numTracks', 'https://schema.org/numTracks'),serialization_alias='https://schema.org/numTracks')
