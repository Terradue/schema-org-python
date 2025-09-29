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

class Painting(CreativeWork):
    '''
    A painting.
    '''
    class_: Literal['https://schema.org/Painting'] = Field( # type: ignore
        default='https://schema.org/Painting',
        alias='@type',
        serialization_alias='@type'
    )
