from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.css_selector_type import CssSelectorType

class SpeakableSpecification(Intangible):
    """
A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property.
    """
    class_: Literal['https://schema.org/SpeakableSpecification'] = Field(default='https://schema.org/SpeakableSpecification', alias='@type', serialization_alias='@type') # type: ignore
    cssSelector: Optional[Union[CssSelectorType, List[CssSelectorType]]] = Field(default=None, validation_alias=AliasChoices('cssSelector', 'https://schema.org/cssSelector'), serialization_alias='https://schema.org/cssSelector')
    xpath: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('xpath', 'https://schema.org/xpath'), serialization_alias='https://schema.org/xpath')
