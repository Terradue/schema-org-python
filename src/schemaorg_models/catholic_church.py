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
from .church import Church

class CatholicChurch(Church):
    '''
    A Catholic church.
    '''
    class_: Literal['https://schema.org/CatholicChurch'] = Field( # type: ignore
        default='https://schema.org/CatholicChurch',
        alias='@type',
        serialization_alias='@type'
    )
