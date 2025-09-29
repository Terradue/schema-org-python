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
from .government_building import GovernmentBuilding

class Embassy(GovernmentBuilding):
    '''
    An embassy.
    '''
    class_: Literal['https://schema.org/Embassy'] = Field( # type: ignore
        default='https://schema.org/Embassy',
        alias='@type',
        serialization_alias='@type'
    )
