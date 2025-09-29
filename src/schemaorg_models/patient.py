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
from .medical_audience import MedicalAudience
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .drug import Drug
    from .medical_condition import MedicalCondition

class Patient(MedicalAudience):
    '''
    A patient is any person recipient of health care services.

    Attributes:
        healthCondition: Specifying the health condition(s) of a patient, medical study, or other target audience.
        diagnosis: One or more alternative conditions considered in the differential diagnosis process as output of a diagnosis process.
        drug: Specifying a drug or medicine used in a medication procedure.
    '''
    class_: Literal['https://schema.org/Patient'] = Field( # type: ignore
        default='https://schema.org/Patient',
        alias='@type',
        serialization_alias='@type'
    )
    healthCondition: Optional[Union['MedicalCondition', List['MedicalCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    diagnosis: Optional[Union['MedicalCondition', List['MedicalCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    drug: Optional[Union['Drug', List['Drug']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
