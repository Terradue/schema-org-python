from __future__ import annotations

from .government_building import GovernmentBuilding    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DefenceEstablishment(GovernmentBuilding):
    """
A defence establishment, such as an army or navy base.
    """
    class_: Literal['https://schema.org/DefenceEstablishment'] = Field( # type: ignore
        default='https://schema.org/DefenceEstablishment',
        alias='@type',
        serialization_alias='@type'
    )
