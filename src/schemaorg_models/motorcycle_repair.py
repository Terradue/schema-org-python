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
from .automotive_business import AutomotiveBusiness

class MotorcycleRepair(AutomotiveBusiness):
    '''
    A motorcycle repair shop.
    '''
    class_: Literal['https://schema.org/MotorcycleRepair'] = Field( # type: ignore
        default='https://schema.org/MotorcycleRepair',
        alias='@type',
        serialization_alias='@type'
    )
