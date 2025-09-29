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

class Brewery(FoodEstablishment):
    '''
    Brewery.
    '''
    class_: Literal['https://schema.org/Brewery'] = Field( # type: ignore
        default='https://schema.org/Brewery',
        alias='@type',
        serialization_alias='@type'
    )
