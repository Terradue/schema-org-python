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

class Reservoir(BodyOfWater):
    """
A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.
    """
    class_: Literal['https://schema.org/Reservoir'] = Field( # type: ignore
        default='https://schema.org/Reservoir',
        alias='@type',
        serialization_alias='@type'
    )
