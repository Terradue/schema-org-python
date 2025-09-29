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
from .local_business import LocalBusiness

class SportsActivityLocation(LocalBusiness):
    '''
    A sports location, such as a playing field.
    '''
    class_: Literal['https://schema.org/SportsActivityLocation'] = Field( # type: ignore
        default='https://schema.org/SportsActivityLocation',
        alias='@type',
        serialization_alias='@type'
    )
