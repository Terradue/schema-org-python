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

class Season(CreativeWork):
    '''
    A media season, e.g. TV, radio, video game etc.
    '''
    class_: Literal['https://schema.org/Season'] = Field( # type: ignore
        default='https://schema.org/Season',
        alias='@type',
        serialization_alias='@type'
    )
