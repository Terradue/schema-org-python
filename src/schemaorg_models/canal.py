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

class Canal(BodyOfWater):
    """
A canal, like the Panama Canal.
    """
    class_: Literal['https://schema.org/Canal'] = Field( # type: ignore
        default='https://schema.org/Canal',
        alias='@type',
        serialization_alias='@type'
    )
