from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.civic_structure import CivicStructure

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
from schemaorg_models.dataset import Dataset
from schemaorg_models.medical_procedure import MedicalProcedure
from schemaorg_models.medical_test import MedicalTest

class Hospital(CivicStructure):
    """
A hospital.
    """
    class_: Literal['https://schema.org/Hospital'] = Field( # type: ignore
        default='https://schema.org/Hospital',
        alias='@type',
        serialization_alias='@type'
    )
    healthcareReportingData: Optional[Union[Dataset, List[Dataset], "CDCPMDRecord", List["CDCPMDRecord"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthcareReportingData',
            'https://schema.org/healthcareReportingData'
        ),
        serialization_alias='https://schema.org/healthcareReportingData'
    )
    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'medicalSpecialty',
            'https://schema.org/medicalSpecialty'
        ),
        serialization_alias='https://schema.org/medicalSpecialty'
    )
    availableService: Optional[Union[MedicalProcedure, List[MedicalProcedure], "MedicalTherapy", List["MedicalTherapy"], MedicalTest, List[MedicalTest]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableService',
            'https://schema.org/availableService'
        ),
        serialization_alias='https://schema.org/availableService'
    )
