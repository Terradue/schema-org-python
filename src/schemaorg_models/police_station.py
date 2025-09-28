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

class PoliceStation(CivicStructure):
    """
A police station.
    """
    class_: Literal['https://schema.org/PoliceStation'] = Field( # type: ignore
        default='https://schema.org/PoliceStation',
        alias='@type',
        serialization_alias='@type'
    )
