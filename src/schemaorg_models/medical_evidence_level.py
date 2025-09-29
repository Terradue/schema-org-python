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

class MedicalEvidenceLevel(MedicalEnumeration):
    '''
    Level of evidence for a medical guideline. Enumerated type.
    '''
    class_: Literal['https://schema.org/MedicalEvidenceLevel'] = Field( # type: ignore
        default='https://schema.org/MedicalEvidenceLevel',
        alias='@type',
        serialization_alias='@type'
    )
