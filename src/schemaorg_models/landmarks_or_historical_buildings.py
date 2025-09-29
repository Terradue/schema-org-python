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
from .place import Place

class LandmarksOrHistoricalBuildings(Place):
    '''
    An historical landmark or building.
    '''
    class_: Literal['https://schema.org/LandmarksOrHistoricalBuildings'] = Field( # type: ignore
        default='https://schema.org/LandmarksOrHistoricalBuildings',
        alias='@type',
        serialization_alias='@type'
    )
