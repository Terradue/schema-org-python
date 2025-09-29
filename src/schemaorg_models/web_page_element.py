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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .css_selector_type import CssSelectorType

class WebPageElement(CreativeWork):
    '''
    A web page element, like a table or an image.

    Attributes:
        xpath: An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
        cssSelector: A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
    '''
    class_: Literal['https://schema.org/WebPageElement'] = Field( # type: ignore
        default='https://schema.org/WebPageElement',
        alias='@type',
        serialization_alias='@type'
    )
    xpath: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    cssSelector: Optional[Union['CssSelectorType', List['CssSelectorType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
