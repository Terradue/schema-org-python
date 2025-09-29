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
from .audience import Audience

class Researcher(Audience):
    '''
    Researchers.
    '''
    class_: Literal['https://schema.org/Researcher'] = Field( # type: ignore
        default='https://schema.org/Researcher',
        alias='@type',
        serialization_alias='@type'
    )
