from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.place_of_worship import PlaceOfWorship

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HinduTemple(PlaceOfWorship):
    """
A Hindu temple.
    """
    class_: Literal['https://schema.org/HinduTemple'] = Field( # type: ignore
        default='https://schema.org/HinduTemple',
        alias='@type',
        serialization_alias='@type'
    )
