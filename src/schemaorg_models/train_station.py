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

class TrainStation(CivicStructure):
    """
A train station.
    """
    class_: Literal['https://schema.org/TrainStation'] = Field( # type: ignore
        default='https://schema.org/TrainStation',
        alias='@type',
        serialization_alias='@type'
    )
