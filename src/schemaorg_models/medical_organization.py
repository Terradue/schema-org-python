from __future__ import annotations

from .organization import Organization    

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

class MedicalOrganization(Organization):
    """
A medical organization (physical or not), such as hospital, institution or clinic.
    """
    class_: Literal['https://schema.org/MedicalOrganization'] = Field( # type: ignore
        default='https://schema.org/MedicalOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    healthPlanNetworkId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanNetworkId',
            'https://schema.org/healthPlanNetworkId'
        ),
        serialization_alias='https://schema.org/healthPlanNetworkId'
    )
    isAcceptingNewPatients: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAcceptingNewPatients',
            'https://schema.org/isAcceptingNewPatients'
        ),
        serialization_alias='https://schema.org/isAcceptingNewPatients'
    )
    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'medicalSpecialty',
            'https://schema.org/medicalSpecialty'
        ),
        serialization_alias='https://schema.org/medicalSpecialty'
    )
