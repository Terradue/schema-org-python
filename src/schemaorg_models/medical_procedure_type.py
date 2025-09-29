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

class MedicalProcedureType(MedicalEnumeration):
    '''
    An enumeration that describes different types of medical procedures.
    '''
    class_: Literal['https://schema.org/MedicalProcedureType'] = Field( # type: ignore
        default='https://schema.org/MedicalProcedureType',
        alias='@type',
        serialization_alias='@type'
    )
