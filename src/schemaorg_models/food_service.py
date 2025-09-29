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
from .service import Service

class FoodService(Service):
    '''
    A food service, like breakfast, lunch, or dinner.
    '''
    class_: Literal['https://schema.org/FoodService'] = Field( # type: ignore
        default='https://schema.org/FoodService',
        alias='@type',
        serialization_alias='@type'
    )
