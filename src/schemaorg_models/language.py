from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Language(Intangible):
    """
A sub property of instrument. The language used on this action.
    """
    class_: Literal['https://schema.org/Language'] = Field( # type: ignore
        default='https://schema.org/Language',
        alias='@type',
        serialization_alias='@type'
    )
