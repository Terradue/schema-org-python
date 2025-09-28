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
from .person import Person
from .creative_work import CreativeWork

class ComicStory(CreativeWork):
    """
The term "story" is any indivisible, re-printable
    	unit of a comic, including the interior stories, covers, and backmatter. Most
    	comics have at least two stories: a cover (ComicCoverArt) and an interior story.
    """
    class_: Literal['https://schema.org/ComicStory'] = Field( # type: ignore
        default='https://schema.org/ComicStory',
        alias='@type',
        serialization_alias='@type'
    )
    penciler: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'penciler',
            'https://schema.org/penciler'
        ),
        serialization_alias='https://schema.org/penciler'
    )
    inker: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inker',
            'https://schema.org/inker'
        ),
        serialization_alias='https://schema.org/inker'
    )
    letterer: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'letterer',
            'https://schema.org/letterer'
        ),
        serialization_alias='https://schema.org/letterer'
    )
    colorist: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'colorist',
            'https://schema.org/colorist'
        ),
        serialization_alias='https://schema.org/colorist'
    )
    artist: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'artist',
            'https://schema.org/artist'
        ),
        serialization_alias='https://schema.org/artist'
    )
