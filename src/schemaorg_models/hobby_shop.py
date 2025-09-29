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

class HobbyShop(Store):
    '''
    A store that sells materials useful or necessary for various hobbies.
    '''
    class_: Literal['https://schema.org/HobbyShop'] = Field( # type: ignore
        default='https://schema.org/HobbyShop',
        alias='@type',
        serialization_alias='@type'
    )
