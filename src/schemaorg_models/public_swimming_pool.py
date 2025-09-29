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
from .sports_activity_location import SportsActivityLocation

class PublicSwimmingPool(SportsActivityLocation):
    '''
    A public swimming pool.
    '''
    class_: Literal['https://schema.org/PublicSwimmingPool'] = Field( # type: ignore
        default='https://schema.org/PublicSwimmingPool',
        alias='@type',
        serialization_alias='@type'
    )
