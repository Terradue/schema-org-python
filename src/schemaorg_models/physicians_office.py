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
from .physician import Physician

class PhysiciansOffice(Physician):
    '''
    A doctor's office or clinic.
    '''
    class_: Literal['https://schema.org/PhysiciansOffice'] = Field( # type: ignore
        default='https://schema.org/PhysiciansOffice',
        alias='@type',
        serialization_alias='@type'
    )
