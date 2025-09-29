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

class Cooperative(Organization):
    '''
    An organization that is a joint project of multiple organizations or persons.
    '''
    class_: Literal['https://schema.org/Cooperative'] = Field( # type: ignore
        default='https://schema.org/Cooperative',
        alias='@type',
        serialization_alias='@type'
    )
