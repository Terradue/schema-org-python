from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.place import Place

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LandmarksOrHistoricalBuildings(Place):
    """
An historical landmark or building.
    """
    class_: Literal['https://schema.org/LandmarksOrHistoricalBuildings'] = Field( # type: ignore
        default='https://schema.org/LandmarksOrHistoricalBuildings',
        alias='@type',
        serialization_alias='@type'
    )
