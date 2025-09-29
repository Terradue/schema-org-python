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

class Courthouse(GovernmentBuilding):
    '''
    A courthouse.
    '''
    class_: Literal['https://schema.org/Courthouse'] = Field( # type: ignore
        default='https://schema.org/Courthouse',
        alias='@type',
        serialization_alias='@type'
    )
