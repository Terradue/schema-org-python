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
from .event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .defined_term import DefinedTerm

class EducationEvent(Event):
    '''
    Event type: Education event.

    Attributes:
        educationalLevel: The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.
        assesses: The item being described is intended to assess the competency or learning outcome defined by the referenced term.
        teaches: The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.
    '''
    class_: Literal['https://schema.org/EducationEvent'] = Field( # type: ignore
        default='https://schema.org/EducationEvent',
        alias='@type',
        serialization_alias='@type'
    )
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    assesses: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    teaches: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
