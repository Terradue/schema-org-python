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
from .media_object import MediaObject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .property_value import PropertyValue

class ImageObject(MediaObject):
    '''
    An image file.

    Attributes:
        representativeOfPage: Indicates whether this image is representative of the content of the page.
        caption: The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        embeddedTextCaption: Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
        exifData: exif data for this object.
    '''
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
    caption: Optional[Union['MediaObject', List['MediaObject'], str, List[str]]] = Field(
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
    exifData: Optional[Union['PropertyValue', List['PropertyValue'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exifData',
            'https://schema.org/exifData'
        ),
        serialization_alias='https://schema.org/exifData'
    )
