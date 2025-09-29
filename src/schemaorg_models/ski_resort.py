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
from .resort import Resort

class SkiResort(Resort):
    '''
    A ski resort.
    '''
    class_: Literal['https://schema.org/SkiResort'] = Field( # type: ignore
        default='https://schema.org/SkiResort',
        alias='@type',
        serialization_alias='@type'
    )
