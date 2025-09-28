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

class SeaBodyOfWater(BodyOfWater):
    """
A sea (for example, the Caspian sea).
    """
    class_: Literal['https://schema.org/SeaBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/SeaBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
