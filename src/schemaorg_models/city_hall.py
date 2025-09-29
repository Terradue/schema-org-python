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

class CityHall(GovernmentBuilding):
    '''
    A city hall.
    '''
    class_: Literal['https://schema.org/CityHall'] = Field( # type: ignore
        default='https://schema.org/CityHall',
        alias='@type',
        serialization_alias='@type'
    )
