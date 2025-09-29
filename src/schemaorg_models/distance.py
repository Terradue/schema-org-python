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
from .quantity import Quantity

class Distance(Quantity):
    '''
    Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.
    '''
    class_: Literal['https://schema.org/Distance'] = Field( # type: ignore
        default='https://schema.org/Distance',
        alias='@type',
        serialization_alias='@type'
    )
