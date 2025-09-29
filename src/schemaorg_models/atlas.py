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

class Atlas(CreativeWork):
    '''
    A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject.
    '''
    class_: Literal['https://schema.org/Atlas'] = Field( # type: ignore
        default='https://schema.org/Atlas',
        alias='@type',
        serialization_alias='@type'
    )
