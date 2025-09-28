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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .css_selector_type import CssSelectorType

class SpeakableSpecification(Intangible):
    """
A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property.
    """
    class_: Literal['https://schema.org/SpeakableSpecification'] = Field( # type: ignore
        default='https://schema.org/SpeakableSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    cssSelector: Optional[Union["CssSelectorType", List["CssSelectorType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cssSelector',
            'https://schema.org/cssSelector'
        ),
        serialization_alias='https://schema.org/cssSelector'
    )
    xpath: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'xpath',
            'https://schema.org/xpath'
        ),
        serialization_alias='https://schema.org/xpath'
    )
