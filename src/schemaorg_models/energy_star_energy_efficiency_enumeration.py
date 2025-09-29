from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .energy_efficiency_enumeration import EnergyEfficiencyEnumeration

class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    '''
    Used to indicate whether a product is EnergyStar certified.
    '''
    class_: Literal['https://schema.org/EnergyStarEnergyEfficiencyEnumeration'] = Field( # type: ignore
        default='https://schema.org/EnergyStarEnergyEfficiencyEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
