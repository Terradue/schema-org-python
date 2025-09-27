from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.text import Text


class CssSelectorType(Text):
    """
Text representing a CSS selector.
    """
    type_: Literal['https://schema.org/CssSelectorType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CssSelectorType'),serialization_alias='class') # type: ignore
