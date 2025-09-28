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

class Electrician(HomeAndConstructionBusiness):
    """
An electrician.
    """
    class_: Literal['https://schema.org/Electrician'] = Field( # type: ignore
        default='https://schema.org/Electrician',
        alias='@type',
        serialization_alias='@type'
    )
