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
from .organization import Organization

class Consortium(Organization):
    '''
    A Consortium is a membership [[Organization]] whose members are typically Organizations.
    '''
    class_: Literal['https://schema.org/Consortium'] = Field( # type: ignore
        default='https://schema.org/Consortium',
        alias='@type',
        serialization_alias='@type'
    )
