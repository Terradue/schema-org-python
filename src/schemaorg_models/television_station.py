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
from .local_business import LocalBusiness

class TelevisionStation(LocalBusiness):
    '''
    A television station.
    '''
    class_: Literal['https://schema.org/TelevisionStation'] = Field( # type: ignore
        default='https://schema.org/TelevisionStation',
        alias='@type',
        serialization_alias='@type'
    )
