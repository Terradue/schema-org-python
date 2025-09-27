from typing import Literal
from pydantic import Field
from schemaorg_models.text import Text


class CssSelectorType(Text):
    """
Text representing a CSS selector.
    """
    class_: Literal['https://schema.org/CssSelectorType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
