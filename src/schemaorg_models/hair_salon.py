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
from .health_and_beauty_business import HealthAndBeautyBusiness

class HairSalon(HealthAndBeautyBusiness):
    '''
    A hair salon.
    '''
    class_: Literal['https://schema.org/HairSalon'] = Field( # type: ignore
        default='https://schema.org/HairSalon',
        alias='@type',
        serialization_alias='@type'
    )
