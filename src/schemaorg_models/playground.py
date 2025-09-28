from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.civic_structure import CivicStructure

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Playground(CivicStructure):
    """
A playground.
    """
    class_: Literal['https://schema.org/Playground'] = Field( # type: ignore
        default='https://schema.org/Playground',
        alias='@type',
        serialization_alias='@type'
    )
