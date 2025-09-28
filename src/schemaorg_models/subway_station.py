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

class SubwayStation(CivicStructure):
    """
A subway station.
    """
    class_: Literal['https://schema.org/SubwayStation'] = Field( # type: ignore
        default='https://schema.org/SubwayStation',
        alias='@type',
        serialization_alias='@type'
    )
