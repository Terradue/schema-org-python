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
from .food_establishment import FoodEstablishment

class Distillery(FoodEstablishment):
    '''
    A distillery.
    '''
    class_: Literal['https://schema.org/Distillery'] = Field( # type: ignore
        default='https://schema.org/Distillery',
        alias='@type',
        serialization_alias='@type'
    )
