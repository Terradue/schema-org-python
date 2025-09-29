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
from .medical_enumeration import MedicalEnumeration

class MedicineSystem(MedicalEnumeration):
    '''
    Systems of medical practice.
    '''
    class_: Literal['https://schema.org/MedicineSystem'] = Field( # type: ignore
        default='https://schema.org/MedicineSystem',
        alias='@type',
        serialization_alias='@type'
    )
