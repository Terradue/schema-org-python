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

class AudioObject(MediaObject):
    '''
    An audio file.

    Attributes:
        transcript: If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
        caption: The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        embeddedTextCaption: Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
    '''
    class_: Literal['https://schema.org/AudioObject'] = Field( # type: ignore
        default='https://schema.org/AudioObject',
        alias='@type',
        serialization_alias='@type'
    )
    transcript: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    caption: Optional[Union['MediaObject', List['MediaObject'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    embeddedTextCaption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
