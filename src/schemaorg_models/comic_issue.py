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
from .publication_issue import PublicationIssue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person

class ComicIssue(PublicationIssue):
    '''
    Individual comic issues are serially published as
    	part of a larger series. For the sake of consistency, even one-shot issues
    	belong to a series comprised of a single issue. All comic issues can be
    	uniquely identified by: the combination of the name and volume number of the
    	series to which the issue belongs; the issue number; and the variant
    	description of the issue (if any).

    Attributes:
        variantCover: A description of the variant cover
    	for the issue, if the issue is a variant printing. For example, "Bryan Hitch
    	Variant Cover" or "2nd Printing Variant".
        colorist: The individual who adds color to inked drawings.
        artist: The primary artist for a work
    	in a medium other than pencils or digital line art--for example, if the
    	primary artwork is done in watercolors or digital paints.
        penciler: The individual who draws the primary narrative artwork.
        inker: The individual who traces over the pencil drawings in ink after pencils are complete.
        letterer: The individual who adds lettering, including speech balloons and sound effects, to artwork.
    '''
    class_: Literal['https://schema.org/ComicIssue'] = Field( # type: ignore
        default='https://schema.org/ComicIssue',
        alias='@type',
        serialization_alias='@type'
    )
    variantCover: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    colorist: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    artist: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    penciler: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    inker: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    letterer: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
