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
from .medical_sign_or_symptom import MedicalSignOrSymptom
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_test import MedicalTest
    from .physical_exam import PhysicalExam

class MedicalSign(MedicalSignOrSymptom):
    '''
    Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.

    Attributes:
        identifyingTest: A diagnostic test that can identify this sign.
        identifyingExam: A physical examination that can identify this sign.
    '''
    class_: Literal['https://schema.org/MedicalSign'] = Field( # type: ignore
        default='https://schema.org/MedicalSign',
        alias='@type',
        serialization_alias='@type'
    )
    identifyingTest: Optional[Union['MedicalTest', List['MedicalTest']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    identifyingExam: Optional[Union['PhysicalExam', List['PhysicalExam']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
