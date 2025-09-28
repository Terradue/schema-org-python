from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.body_of_water import BodyOfWater

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RiverBodyOfWater(BodyOfWater):
    """
A river (for example, the broad majestic Shannon).
    """
    class_: Literal['https://schema.org/RiverBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/RiverBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
