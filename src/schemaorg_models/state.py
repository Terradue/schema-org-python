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
from .administrative_area import AdministrativeArea

class State(AdministrativeArea):
    '''
    A state or province of a country.
    '''
    class_: Literal['https://schema.org/State'] = Field( # type: ignore
        default='https://schema.org/State',
        alias='@type',
        serialization_alias='@type'
    )
