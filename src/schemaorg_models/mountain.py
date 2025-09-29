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
from .landform import Landform

class Mountain(Landform):
    '''
    A mountain, like Mount Whitney or Mount Everest.
    '''
    class_: Literal['https://schema.org/Mountain'] = Field( # type: ignore
        default='https://schema.org/Mountain',
        alias='@type',
        serialization_alias='@type'
    )
