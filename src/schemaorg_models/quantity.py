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
from .intangible import Intangible

class Quantity(Intangible):
    '''
    Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.
    '''
    class_: Literal['https://schema.org/Quantity'] = Field( # type: ignore
        default='https://schema.org/Quantity',
        alias='@type',
        serialization_alias='@type'
    )
