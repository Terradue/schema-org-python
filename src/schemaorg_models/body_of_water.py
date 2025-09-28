from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.landform import Landform

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BodyOfWater(Landform):
    """
A body of water, such as a sea, ocean, or lake.
    """
    class_: Literal['https://schema.org/BodyOfWater'] = Field( # type: ignore
        default='https://schema.org/BodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
