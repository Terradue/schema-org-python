from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.media_object import MediaObject

from schemaorg_models.media_object import MediaObject

class AudioObject(MediaObject):
    """
An audio file.
    """
    transcript: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('transcript', 'https://schema.org/transcript'),serialization_alias='https://schema.org/transcript')
    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('caption', 'https://schema.org/caption'),serialization_alias='https://schema.org/caption')
    embeddedTextCaption: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('embeddedTextCaption', 'https://schema.org/embeddedTextCaption'),serialization_alias='https://schema.org/embeddedTextCaption')
