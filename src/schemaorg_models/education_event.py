from __future__ import annotations
from pydantic import (
    AliasChoices,
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
    """
Event type: Education event.
    """
    class_: Literal['https://schema.org/EducationEvent'] = Field( # type: ignore
        default='https://schema.org/EducationEvent',
        alias='@type',
        serialization_alias='@type'
    )
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalLevel',
            'https://schema.org/educationalLevel'
        ),
        serialization_alias='https://schema.org/educationalLevel'
    )
    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'assesses',
            'https://schema.org/assesses'
        ),
        serialization_alias='https://schema.org/assesses'
    )
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'teaches',
            'https://schema.org/teaches'
        ),
        serialization_alias='https://schema.org/teaches'
    )
