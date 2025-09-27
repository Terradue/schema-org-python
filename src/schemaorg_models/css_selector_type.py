from typing import Literal
from pydantic import Field
from schemaorg_models.text import Text


class CssSelectorType(Text):
    """
Text representing a CSS selector.
    """
    type_: Literal['https://schema.org/CssSelectorType'] = Field(default='https://schema.org/CssSelectorType', alias='@type', serialization_alias='@type') # type: ignore
