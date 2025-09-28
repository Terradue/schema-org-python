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

class Volcano(Landform):
    """
A volcano, like Fujisan.
    """
    class_: Literal['https://schema.org/Volcano'] = Field( # type: ignore
        default='https://schema.org/Volcano',
        alias='@type',
        serialization_alias='@type'
    )
