from __future__ import annotations

from .performing_group import PerformingGroup    

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
