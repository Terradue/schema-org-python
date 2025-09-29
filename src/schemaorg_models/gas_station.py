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

class GasStation(AutomotiveBusiness):
    '''
    A gas station.
    '''
    class_: Literal['https://schema.org/GasStation'] = Field( # type: ignore
        default='https://schema.org/GasStation',
        alias='@type',
        serialization_alias='@type'
    )
