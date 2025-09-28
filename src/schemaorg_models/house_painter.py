from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HousePainter(HomeAndConstructionBusiness):
    """
A house painting service.
    """
    class_: Literal['https://schema.org/HousePainter'] = Field( # type: ignore
        default='https://schema.org/HousePainter',
        alias='@type',
        serialization_alias='@type'
    )
