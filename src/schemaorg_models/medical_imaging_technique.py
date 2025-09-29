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

class MedicalImagingTechnique(MedicalEnumeration):
    '''
    Any medical imaging modality typically used for diagnostic purposes. Enumerated type.
    '''
    class_: Literal['https://schema.org/MedicalImagingTechnique'] = Field( # type: ignore
        default='https://schema.org/MedicalImagingTechnique',
        alias='@type',
        serialization_alias='@type'
    )
