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

class DrugPrescriptionStatus(MedicalEnumeration):
    '''
    Indicates whether this drug is available by prescription or over-the-counter.
    '''
    class_: Literal['https://schema.org/DrugPrescriptionStatus'] = Field( # type: ignore
        default='https://schema.org/DrugPrescriptionStatus',
        alias='@type',
        serialization_alias='@type'
    )
