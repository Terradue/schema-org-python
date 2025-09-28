from __future__ import annotations

from .creative_work_season import CreativeWorkSeason    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RadioSeason(CreativeWorkSeason):
    """
Season dedicated to radio broadcast and associated online delivery.
    """
    class_: Literal['https://schema.org/RadioSeason'] = Field( # type: ignore
        default='https://schema.org/RadioSeason',
        alias='@type',
        serialization_alias='@type'
    )
