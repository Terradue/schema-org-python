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

class TierBenefitEnumeration(Enumeration):
    '''
    An enumeration of possible benefits as part of a loyalty (members) program.
    '''
    class_: Literal['https://schema.org/TierBenefitEnumeration'] = Field( # type: ignore
        default='https://schema.org/TierBenefitEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
