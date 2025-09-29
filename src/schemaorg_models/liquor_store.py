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

class LiquorStore(Store):
    '''
    A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.
    '''
    class_: Literal['https://schema.org/LiquorStore'] = Field( # type: ignore
        default='https://schema.org/LiquorStore',
        alias='@type',
        serialization_alias='@type'
    )
