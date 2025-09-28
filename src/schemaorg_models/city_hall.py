from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.government_building import GovernmentBuilding

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CityHall(GovernmentBuilding):
    """
A city hall.
    """
    class_: Literal['https://schema.org/CityHall'] = Field( # type: ignore
        default='https://schema.org/CityHall',
        alias='@type',
        serialization_alias='@type'
    )
