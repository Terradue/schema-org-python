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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .css_selector_type import CssSelectorType

class WebPageElement(CreativeWork):
    """
A web page element, like a table or an image.
    """
    class_: Literal['https://schema.org/WebPageElement'] = Field( # type: ignore
        default='https://schema.org/WebPageElement',
        alias='@type',
        serialization_alias='@type'
    )
    xpath: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'xpath',
            'https://schema.org/xpath'
        ),
        serialization_alias='https://schema.org/xpath'
    )
    cssSelector: Optional[Union["CssSelectorType", List["CssSelectorType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cssSelector',
            'https://schema.org/cssSelector'
        ),
        serialization_alias='https://schema.org/cssSelector'
    )
