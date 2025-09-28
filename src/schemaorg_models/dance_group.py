from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.performing_group import PerformingGroup

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DanceGroup(PerformingGroup):
    """
A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.
    """
    class_: Literal['https://schema.org/DanceGroup'] = Field( # type: ignore
        default='https://schema.org/DanceGroup',
        alias='@type',
        serialization_alias='@type'
    )
