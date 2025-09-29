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
from .quantity import Quantity

class Duration(Quantity):
    '''
    Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).
    '''
    class_: Literal['https://schema.org/Duration'] = Field( # type: ignore
        default='https://schema.org/Duration',
        alias='@type',
        serialization_alias='@type'
    )
