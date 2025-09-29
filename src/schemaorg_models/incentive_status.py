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

class IncentiveStatus(Enumeration):
    '''
    Enumerates a status for an incentive, such as whether it is active.
    '''
    class_: Literal['https://schema.org/IncentiveStatus'] = Field( # type: ignore
        default='https://schema.org/IncentiveStatus',
        alias='@type',
        serialization_alias='@type'
    )
