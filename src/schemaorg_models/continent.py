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

class Continent(Landform):
    """
One of the continents (for example, Europe or Africa).
    """
    class_: Literal['https://schema.org/Continent'] = Field( # type: ignore
        default='https://schema.org/Continent',
        alias='@type',
        serialization_alias='@type'
    )
