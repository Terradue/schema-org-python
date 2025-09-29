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
from .medical_business import MedicalBusiness

class Dentist(MedicalBusiness):
    '''
    A dentist.
    '''
    class_: Literal['https://schema.org/Dentist'] = Field( # type: ignore
        default='https://schema.org/Dentist',
        alias='@type',
        serialization_alias='@type'
    )
