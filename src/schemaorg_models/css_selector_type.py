from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.text import Text

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CssSelectorType(Text):
    """
Text representing a CSS selector.
    """
    class_: Literal['https://schema.org/CssSelectorType'] = Field( # type: ignore
        default='https://schema.org/CssSelectorType',
        alias='@type',
        serialization_alias='@type'
    )
