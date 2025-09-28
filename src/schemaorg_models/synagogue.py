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

class Synagogue(PlaceOfWorship):
    """
A synagogue.
    """
    class_: Literal['https://schema.org/Synagogue'] = Field( # type: ignore
        default='https://schema.org/Synagogue',
        alias='@type',
        serialization_alias='@type'
    )
