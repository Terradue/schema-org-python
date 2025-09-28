from __future__ import annotations

from .government_building import GovernmentBuilding    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Embassy(GovernmentBuilding):
    """
An embassy.
    """
    class_: Literal['https://schema.org/Embassy'] = Field( # type: ignore
        default='https://schema.org/Embassy',
        alias='@type',
        serialization_alias='@type'
    )
