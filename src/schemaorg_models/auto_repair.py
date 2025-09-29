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
from .automotive_business import AutomotiveBusiness

class AutoRepair(AutomotiveBusiness):
    '''
    Car repair business.
    '''
    class_: Literal['https://schema.org/AutoRepair'] = Field( # type: ignore
        default='https://schema.org/AutoRepair',
        alias='@type',
        serialization_alias='@type'
    )
