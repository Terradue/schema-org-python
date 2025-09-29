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

class BarOrPub(FoodEstablishment):
    '''
    A bar or pub.
    '''
    class_: Literal['https://schema.org/BarOrPub'] = Field( # type: ignore
        default='https://schema.org/BarOrPub',
        alias='@type',
        serialization_alias='@type'
    )
