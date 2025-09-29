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
from .medical_sign import MedicalSign

class VitalSign(MedicalSign):
    '''
    Vital signs are measures of various physiological functions in order to assess the most basic body functions.
    '''
    class_: Literal['https://schema.org/VitalSign'] = Field( # type: ignore
        default='https://schema.org/VitalSign',
        alias='@type',
        serialization_alias='@type'
    )
