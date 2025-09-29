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

class LegislativeBuilding(GovernmentBuilding):
    '''
    A legislative building&#x2014;for example, the state capitol.
    '''
    class_: Literal['https://schema.org/LegislativeBuilding'] = Field( # type: ignore
        default='https://schema.org/LegislativeBuilding',
        alias='@type',
        serialization_alias='@type'
    )
