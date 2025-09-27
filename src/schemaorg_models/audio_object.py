from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.media_object import MediaObject

from schemaorg_models.media_object import MediaObject

class AudioObject(MediaObject):
    """
An audio file.
    """
    class_: Literal['https://schema.org/AudioObject'] = Field(default='https://schema.org/AudioObject', alias='@type', serialization_alias='@type') # type: ignore
    transcript: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('transcript', 'https://schema.org/transcript'), serialization_alias='https://schema.org/transcript')
    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('caption', 'https://schema.org/caption'), serialization_alias='https://schema.org/caption')
    embeddedTextCaption: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('embeddedTextCaption', 'https://schema.org/embeddedTextCaption'), serialization_alias='https://schema.org/embeddedTextCaption')
