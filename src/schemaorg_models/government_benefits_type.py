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

class GovernmentBenefitsType(Enumeration):
    '''
    GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered.
    '''
    class_: Literal['https://schema.org/GovernmentBenefitsType'] = Field( # type: ignore
        default='https://schema.org/GovernmentBenefitsType',
        alias='@type',
        serialization_alias='@type'
    )
