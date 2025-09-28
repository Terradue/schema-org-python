from __future__ import annotations

from .medical_business import MedicalBusiness    

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
from schemaorg_models.hospital import Hospital
from schemaorg_models.medical_procedure import MedicalProcedure
from schemaorg_models.medical_test import MedicalTest
from schemaorg_models.category_code import CategoryCode

class Physician(MedicalBusiness):
    """
An individual physician or a physician's office considered as a [[MedicalOrganization]].
    """
    class_: Literal['https://schema.org/Physician'] = Field( # type: ignore
        default='https://schema.org/Physician',
        alias='@type',
        serialization_alias='@type'
    )
    hospitalAffiliation: Optional[Union[Hospital, List[Hospital]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hospitalAffiliation',
            'https://schema.org/hospitalAffiliation'
        ),
        serialization_alias='https://schema.org/hospitalAffiliation'
    )
    availableService: Optional[Union[MedicalProcedure, List[MedicalProcedure], "MedicalTherapy", List["MedicalTherapy"], MedicalTest, List[MedicalTest]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableService',
            'https://schema.org/availableService'
        ),
        serialization_alias='https://schema.org/availableService'
    )
    usNPI: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'usNPI',
            'https://schema.org/usNPI'
        ),
        serialization_alias='https://schema.org/usNPI'
    )
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory',
            'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory'
    )
    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'medicalSpecialty',
            'https://schema.org/medicalSpecialty'
        ),
        serialization_alias='https://schema.org/medicalSpecialty'
    )
