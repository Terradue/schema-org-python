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

class Bakery(FoodEstablishment):
    '''
    A bakery.
    '''
    class_: Literal['https://schema.org/Bakery'] = Field( # type: ignore
        default='https://schema.org/Bakery',
        alias='@type',
        serialization_alias='@type'
    )
