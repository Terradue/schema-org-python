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

class Country(AdministrativeArea):
    '''
    A country.
    '''
    class_: Literal['https://schema.org/Country'] = Field( # type: ignore
        default='https://schema.org/Country',
        alias='@type',
        serialization_alias='@type'
    )
