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

class MedicalDevicePurpose(MedicalEnumeration):
    '''
    Categories of medical devices, organized by the purpose or intended use of the device.
    '''
    class_: Literal['https://schema.org/MedicalDevicePurpose'] = Field( # type: ignore
        default='https://schema.org/MedicalDevicePurpose',
        alias='@type',
        serialization_alias='@type'
    )
