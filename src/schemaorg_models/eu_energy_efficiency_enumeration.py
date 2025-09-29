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

class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    '''
    Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.
    '''
    class_: Literal['https://schema.org/EUEnergyEfficiencyEnumeration'] = Field( # type: ignore
        default='https://schema.org/EUEnergyEfficiencyEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
