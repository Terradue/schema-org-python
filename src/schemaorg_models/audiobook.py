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
from .audio_object import AudioObject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .duration import Duration
    from .person import Person

class Audiobook(AudioObject):
    '''
    An audiobook.

    Attributes:
        duration: The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        readBy: A person who reads (performs) the audiobook.
    '''
    class_: Literal['https://schema.org/Audiobook'] = Field( # type: ignore
        default='https://schema.org/Audiobook',
        alias='@type',
        serialization_alias='@type'
    )
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    readBy: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
