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
from .creative_work import CreativeWork

class Sculpture(CreativeWork):
    '''
    A piece of sculpture.
    '''
    class_: Literal['https://schema.org/Sculpture'] = Field( # type: ignore
        default='https://schema.org/Sculpture',
        alias='@type',
        serialization_alias='@type'
    )
