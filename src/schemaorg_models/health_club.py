from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HealthClub(HealthAndBeautyBusiness):
    """
A health club.
    """
    class_: Literal['https://schema.org/HealthClub'] = Field( # type: ignore
        default='https://schema.org/HealthClub',
        alias='@type',
        serialization_alias='@type'
    )
