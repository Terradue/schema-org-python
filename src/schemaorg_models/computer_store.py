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

class ComputerStore(Store):
    '''
    A computer store.
    '''
    class_: Literal['https://schema.org/ComputerStore'] = Field( # type: ignore
        default='https://schema.org/ComputerStore',
        alias='@type',
        serialization_alias='@type'
    )
