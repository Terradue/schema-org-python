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
from .medical_test import MedicalTest

class BloodTest(MedicalTest):
    '''
    A medical test performed on a sample of a patient's blood.
    '''
    class_: Literal['https://schema.org/BloodTest'] = Field( # type: ignore
        default='https://schema.org/BloodTest',
        alias='@type',
        serialization_alias='@type'
    )
