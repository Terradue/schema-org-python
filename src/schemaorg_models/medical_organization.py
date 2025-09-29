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
from .organization import Organization
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_specialty import MedicalSpecialty

class MedicalOrganization(Organization):
    '''
    A medical organization (physical or not), such as hospital, institution or clinic.

    Attributes:
        healthPlanNetworkId: Name or unique ID of network. (Networks are often reused across different insurance plans.)
        isAcceptingNewPatients: Whether the provider is accepting new patients.
        medicalSpecialty: A medical specialty of the provider.
    '''
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
    medicalSpecialty: Optional[Union['MedicalSpecialty', List['MedicalSpecialty']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'medicalSpecialty',
            'https://schema.org/medicalSpecialty'
        ),
        serialization_alias='https://schema.org/medicalSpecialty'
    )
