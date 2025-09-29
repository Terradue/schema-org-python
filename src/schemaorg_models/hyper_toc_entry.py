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
    from .media_object import MediaObject

class HyperTocEntry(CreativeWork):
    '''
    A HyperToEntry is an item within a [[HyperToc]], which represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. The media object itself is indicated using [[associatedMedia]]. Each section of interest within that content can be described with a [[HyperTocEntry]], with associated [[startOffset]] and [[endOffset]]. When several entries are all from the same file, [[associatedMedia]] is used on the overarching [[HyperTocEntry]]; if the content has been split into multiple files, they can be referenced using [[associatedMedia]] on each [[HyperTocEntry]].

    Attributes:
        utterances: Text of an utterances (spoken words, lyrics etc.) that occurs at a certain section of a media object, represented as a [[HyperTocEntry]].
        tocContinuation: A [[HyperTocEntry]] can have a [[tocContinuation]] indicated, which is another [[HyperTocEntry]] that would be the default next item to play or render.
        associatedMedia: A media object that encodes this CreativeWork. This property is a synonym for encoding.
    '''
    class_: Literal['https://schema.org/HyperTocEntry'] = Field( # type: ignore
        default='https://schema.org/HyperTocEntry',
        alias='@type',
        serialization_alias='@type'
    )
    utterances: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    tocContinuation: Optional[Union['HyperTocEntry', List['HyperTocEntry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    associatedMedia: Optional[Union['MediaObject', List['MediaObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
