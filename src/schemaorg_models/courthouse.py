from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .government_building import GovernmentBuilding

class Courthouse(GovernmentBuilding):
    """
A courthouse.
    """
    class_: Literal['https://schema.org/Courthouse'] = Field( # type: ignore
        default='https://schema.org/Courthouse',
        alias='@type',
        serialization_alias='@type'
    )
