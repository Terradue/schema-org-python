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

class AutoWash(AutomotiveBusiness):
    '''
    A car wash business.
    '''
    class_: Literal['https://schema.org/AutoWash'] = Field( # type: ignore
        default='https://schema.org/AutoWash',
        alias='@type',
        serialization_alias='@type'
    )
