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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person

class ComicStory(CreativeWork):
    '''
    The term "story" is any indivisible, re-printable
    	unit of a comic, including the interior stories, covers, and backmatter. Most
    	comics have at least two stories: a cover (ComicCoverArt) and an interior story.

    Attributes:
        penciler: The individual who draws the primary narrative artwork.
        inker: The individual who traces over the pencil drawings in ink after pencils are complete.
        letterer: The individual who adds lettering, including speech balloons and sound effects, to artwork.
        colorist: The individual who adds color to inked drawings.
        artist: The primary artist for a work
    	in a medium other than pencils or digital line art--for example, if the
    	primary artwork is done in watercolors or digital paints.
    '''
    class_: Literal['https://schema.org/ComicStory'] = Field( # type: ignore
        default='https://schema.org/ComicStory',
        alias='@type',
        serialization_alias='@type'
    )
    penciler: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'penciler',
            'https://schema.org/penciler'
        ),
        serialization_alias='https://schema.org/penciler'
    )
    inker: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inker',
            'https://schema.org/inker'
        ),
        serialization_alias='https://schema.org/inker'
    )
    letterer: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'letterer',
            'https://schema.org/letterer'
        ),
        serialization_alias='https://schema.org/letterer'
    )
    colorist: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'colorist',
            'https://schema.org/colorist'
        ),
        serialization_alias='https://schema.org/colorist'
    )
    artist: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'artist',
            'https://schema.org/artist'
        ),
        serialization_alias='https://schema.org/artist'
    )
