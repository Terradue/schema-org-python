from __future__ import annotations

from .creative_work import CreativeWork    

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
from schemaorg_models.item_list import ItemList

class MusicPlaylist(CreativeWork):
    """
A collection of music tracks in playlist form.
    """
    class_: Literal['https://schema.org/MusicPlaylist'] = Field( # type: ignore
        default='https://schema.org/MusicPlaylist',
        alias='@type',
        serialization_alias='@type'
    )
    tracks: Optional[Union["MusicRecording", List["MusicRecording"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tracks',
            'https://schema.org/tracks'
        ),
        serialization_alias='https://schema.org/tracks'
    )
    track: Optional[Union[ItemList, List[ItemList], "MusicRecording", List["MusicRecording"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'track',
            'https://schema.org/track'
        ),
        serialization_alias='https://schema.org/track'
    )
    numTracks: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numTracks',
            'https://schema.org/numTracks'
        ),
        serialization_alias='https://schema.org/numTracks'
    )
