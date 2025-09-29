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
from .thing import Thing

class Intangible(Thing):
    '''
    A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.
    '''
    class_: Literal['https://schema.org/Intangible'] = Field( # type: ignore
        default='https://schema.org/Intangible',
        alias='@type',
        serialization_alias='@type'
    )
