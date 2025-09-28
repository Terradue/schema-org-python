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
from .music_group import MusicGroup
from .media_object import MediaObject
from .person import Person
from .performing_group import PerformingGroup

class VideoObject(MediaObject):
    """
A video file.
    """
    class_: Literal['https://schema.org/VideoObject'] = Field( # type: ignore
        default='https://schema.org/VideoObject',
        alias='@type',
        serialization_alias='@type'
    )
    directors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'directors',
            'https://schema.org/directors'
        ),
        serialization_alias='https://schema.org/directors'
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    videoFrameSize: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'videoFrameSize',
            'https://schema.org/videoFrameSize'
        ),
        serialization_alias='https://schema.org/videoFrameSize'
    )
    actor: Optional[Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    transcript: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transcript',
            'https://schema.org/transcript'
        ),
        serialization_alias='https://schema.org/transcript'
    )
    actors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
    )
    videoQuality: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'videoQuality',
            'https://schema.org/videoQuality'
        ),
        serialization_alias='https://schema.org/videoQuality'
    )
    musicBy: Optional[Union[MusicGroup, List[MusicGroup], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicBy',
            'https://schema.org/musicBy'
        ),
        serialization_alias='https://schema.org/musicBy'
    )
    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'caption',
            'https://schema.org/caption'
        ),
        serialization_alias='https://schema.org/caption'
    )
    embeddedTextCaption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'embeddedTextCaption',
            'https://schema.org/embeddedTextCaption'
        ),
        serialization_alias='https://schema.org/embeddedTextCaption'
    )
