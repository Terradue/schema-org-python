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

class GeneralContractor(HomeAndConstructionBusiness):
    """
A general contractor.
    """
    class_: Literal['https://schema.org/GeneralContractor'] = Field( # type: ignore
        default='https://schema.org/GeneralContractor',
        alias='@type',
        serialization_alias='@type'
    )
