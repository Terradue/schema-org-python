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

class BeautySalon(HealthAndBeautyBusiness):
    '''
    Beauty salon.
    '''
    class_: Literal['https://schema.org/BeautySalon'] = Field( # type: ignore
        default='https://schema.org/BeautySalon',
        alias='@type',
        serialization_alias='@type'
    )
