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

class RoofingContractor(HomeAndConstructionBusiness):
    """
A roofing contractor.
    """
    class_: Literal['https://schema.org/RoofingContractor'] = Field( # type: ignore
        default='https://schema.org/RoofingContractor',
        alias='@type',
        serialization_alias='@type'
    )
