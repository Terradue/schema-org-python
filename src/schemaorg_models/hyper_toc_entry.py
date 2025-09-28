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
from schemaorg_models.media_object import MediaObject

class HyperTocEntry(CreativeWork):
    """
A HyperToEntry is an item within a [[HyperToc]], which represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. The media object itself is indicated using [[associatedMedia]]. Each section of interest within that content can be described with a [[HyperTocEntry]], with associated [[startOffset]] and [[endOffset]]. When several entries are all from the same file, [[associatedMedia]] is used on the overarching [[HyperTocEntry]]; if the content has been split into multiple files, they can be referenced using [[associatedMedia]] on each [[HyperTocEntry]].
    """
    class_: Literal['https://schema.org/HyperTocEntry'] = Field( # type: ignore
        default='https://schema.org/HyperTocEntry',
        alias='@type',
        serialization_alias='@type'
    )
    utterances: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'utterances',
            'https://schema.org/utterances'
        ),
        serialization_alias='https://schema.org/utterances'
    )
    tocContinuation: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tocContinuation',
            'https://schema.org/tocContinuation'
        ),
        serialization_alias='https://schema.org/tocContinuation'
    )
    associatedMedia: Optional[Union[MediaObject, List[MediaObject]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedMedia',
            'https://schema.org/associatedMedia'
        ),
        serialization_alias='https://schema.org/associatedMedia'
    )
