from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.media_object import MediaObject

from schemaorg_models.media_object import MediaObject
from schemaorg_models.property_value import PropertyValue

class ImageObject(MediaObject):
    """
An image file.
    """
    class_: Literal['https://schema.org/ImageObject'] = Field(default='https://schema.org/ImageObject', alias='class', serialization_alias='class') # type: ignore
    representativeOfPage: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('representativeOfPage', 'https://schema.org/representativeOfPage'), serialization_alias='https://schema.org/representativeOfPage')
    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('caption', 'https://schema.org/caption'), serialization_alias='https://schema.org/caption')
    embeddedTextCaption: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('embeddedTextCaption', 'https://schema.org/embeddedTextCaption'), serialization_alias='https://schema.org/embeddedTextCaption')
    exifData: Optional[Union[PropertyValue, List[PropertyValue], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('exifData', 'https://schema.org/exifData'), serialization_alias='https://schema.org/exifData')
