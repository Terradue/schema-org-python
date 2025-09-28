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
from .audio_object import AudioObject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .duration import Duration
    from .quantitative_value import QuantitativeValue
    from .person import Person

class Audiobook(AudioObject):
    """
An audiobook.
    """
    class_: Literal['https://schema.org/Audiobook'] = Field( # type: ignore
        default='https://schema.org/Audiobook',
        alias='@type',
        serialization_alias='@type'
    )
    duration: Optional[Union["Duration", List["Duration"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
    readBy: Optional[Union["Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'readBy',
            'https://schema.org/readBy'
        ),
        serialization_alias='https://schema.org/readBy'
    )
