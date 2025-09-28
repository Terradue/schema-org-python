from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.sports_activity_location import SportsActivityLocation

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TennisComplex(SportsActivityLocation):
    """
A tennis complex.
    """
    class_: Literal['https://schema.org/TennisComplex'] = Field( # type: ignore
        default='https://schema.org/TennisComplex',
        alias='@type',
        serialization_alias='@type'
    )
