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
from .store import Store

class Florist(Store):
    '''
    A florist.
    '''
    class_: Literal['https://schema.org/Florist'] = Field( # type: ignore
        default='https://schema.org/Florist',
        alias='@type',
        serialization_alias='@type'
    )
