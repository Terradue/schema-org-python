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
    from .hyper_toc_entry import HyperTocEntry
    from .media_object import MediaObject

class HyperToc(CreativeWork):
    '''
    A HyperToc represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the same larger work is split into multiple files, [[associatedMedia]] can be used on individual [[HyperTocEntry]] items.

    Attributes:
        tocEntry: Indicates a [[HyperTocEntry]] in a [[HyperToc]].
        associatedMedia: A media object that encodes this CreativeWork. This property is a synonym for encoding.
    '''
    class_: Literal['https://schema.org/HyperToc'] = Field( # type: ignore
        default='https://schema.org/HyperToc',
        alias='@type',
        serialization_alias='@type'
    )
    tocEntry: Optional[Union['HyperTocEntry', List['HyperTocEntry']]] = Field(
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
