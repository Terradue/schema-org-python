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

class Store(LocalBusiness):
    '''
    A retail good store.
    '''
    class_: Literal['https://schema.org/Store'] = Field( # type: ignore
        default='https://schema.org/Store',
        alias='@type',
        serialization_alias='@type'
    )
