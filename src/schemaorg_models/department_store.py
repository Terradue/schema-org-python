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

class DepartmentStore(Store):
    '''
    A department store.
    '''
    class_: Literal['https://schema.org/DepartmentStore'] = Field( # type: ignore
        default='https://schema.org/DepartmentStore',
        alias='@type',
        serialization_alias='@type'
    )
