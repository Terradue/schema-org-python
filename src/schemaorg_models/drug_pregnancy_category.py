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

class DrugPregnancyCategory(MedicalEnumeration):
    '''
    Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.
    '''
    class_: Literal['https://schema.org/DrugPregnancyCategory'] = Field( # type: ignore
        default='https://schema.org/DrugPregnancyCategory',
        alias='@type',
        serialization_alias='@type'
    )
