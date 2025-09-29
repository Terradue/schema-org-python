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
from .enumeration import Enumeration

class EnergyEfficiencyEnumeration(Enumeration):
    '''
    Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.
    '''
    class_: Literal['https://schema.org/EnergyEfficiencyEnumeration'] = Field( # type: ignore
        default='https://schema.org/EnergyEfficiencyEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
