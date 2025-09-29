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

class Photograph(CreativeWork):
    '''
    A photograph.
    '''
    class_: Literal['https://schema.org/Photograph'] = Field( # type: ignore
        default='https://schema.org/Photograph',
        alias='@type',
        serialization_alias='@type'
    )
