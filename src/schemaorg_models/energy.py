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

class Energy(Quantity):
    '''
    Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit of measure&gt;'.
    '''
    class_: Literal['https://schema.org/Energy'] = Field( # type: ignore
        default='https://schema.org/Energy',
        alias='@type',
        serialization_alias='@type'
    )
