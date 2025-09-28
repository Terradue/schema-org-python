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

class Cemetery(CivicStructure):
    """
A graveyard.
    """
    class_: Literal['https://schema.org/Cemetery'] = Field( # type: ignore
        default='https://schema.org/Cemetery',
        alias='@type',
        serialization_alias='@type'
    )
