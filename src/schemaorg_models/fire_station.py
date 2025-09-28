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

class FireStation(CivicStructure):
    """
A fire station. With firemen.
    """
    class_: Literal['https://schema.org/FireStation'] = Field( # type: ignore
        default='https://schema.org/FireStation',
        alias='@type',
        serialization_alias='@type'
    )
