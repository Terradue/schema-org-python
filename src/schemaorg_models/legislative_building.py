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

class LegislativeBuilding(GovernmentBuilding):
    """
A legislative building&#x2014;for example, the state capitol.
    """
    class_: Literal['https://schema.org/LegislativeBuilding'] = Field( # type: ignore
        default='https://schema.org/LegislativeBuilding',
        alias='@type',
        serialization_alias='@type'
    )
