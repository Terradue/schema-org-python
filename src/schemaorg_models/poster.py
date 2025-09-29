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

class Poster(CreativeWork):
    '''
    A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something.
    '''
    class_: Literal['https://schema.org/Poster'] = Field( # type: ignore
        default='https://schema.org/Poster',
        alias='@type',
        serialization_alias='@type'
    )
