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

class TheaterGroup(PerformingGroup):
    """
A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.
    """
    class_: Literal['https://schema.org/TheaterGroup'] = Field( # type: ignore
        default='https://schema.org/TheaterGroup',
        alias='@type',
        serialization_alias='@type'
    )
