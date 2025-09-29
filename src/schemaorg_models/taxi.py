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
from .service import Service

class Taxi(Service):
    '''
    A taxi.
    '''
    class_: Literal['https://schema.org/Taxi'] = Field( # type: ignore
        default='https://schema.org/Taxi',
        alias='@type',
        serialization_alias='@type'
    )
