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

class Drawing(CreativeWork):
    '''
    A picture or diagram made with a pencil, pen, or crayon rather than paint.
    '''
    class_: Literal['https://schema.org/Drawing'] = Field( # type: ignore
        default='https://schema.org/Drawing',
        alias='@type',
        serialization_alias='@type'
    )
