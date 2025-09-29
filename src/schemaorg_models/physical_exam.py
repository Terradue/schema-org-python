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

class PhysicalExam(MedicalEnumeration):
    '''
    A type of physical examination of a patient performed by a physician. 
    '''
    class_: Literal['https://schema.org/PhysicalExam'] = Field( # type: ignore
        default='https://schema.org/PhysicalExam',
        alias='@type',
        serialization_alias='@type'
    )
