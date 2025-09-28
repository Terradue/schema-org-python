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
from .media_object import MediaObject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .property_value import PropertyValue

class ImageObject(MediaObject):
    """
An image file.
    """
    class_: Literal['https://schema.org/ImageObject'] = Field( # type: ignore
        default='https://schema.org/ImageObject',
        alias='@type',
        serialization_alias='@type'
    )
    representativeOfPage: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'representativeOfPage',
            'https://schema.org/representativeOfPage'
        ),
        serialization_alias='https://schema.org/representativeOfPage'
    )
    caption: Optional[Union["MediaObject", List["MediaObject"], str, List[str]]] = Field(
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
    exifData: Optional[Union["PropertyValue", List["PropertyValue"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exifData',
            'https://schema.org/exifData'
        ),
        serialization_alias='https://schema.org/exifData'
    )
