from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .medical_intangible import MedicalIntangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_condition import MedicalCondition
    from .medical_sign_or_symptom import MedicalSignOrSymptom

class DDxElement(MedicalIntangible):
    """
An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.
    """
    class_: Literal['https://schema.org/DDxElement'] = Field( # type: ignore
        default='https://schema.org/DDxElement',
        alias='@type',
        serialization_alias='@type'
    )
    distinguishingSign: Optional[Union["MedicalSignOrSymptom", List["MedicalSignOrSymptom"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distinguishingSign',
            'https://schema.org/distinguishingSign'
        ),
        serialization_alias='https://schema.org/distinguishingSign'
    )
    diagnosis: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diagnosis',
            'https://schema.org/diagnosis'
        ),
        serialization_alias='https://schema.org/diagnosis'
    )
