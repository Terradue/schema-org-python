from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure

from schemaorg_models.dataset import Dataset
from schemaorg_models.medical_procedure import MedicalProcedure
from schemaorg_models.medical_test import MedicalTest

class Hospital(CivicStructure):
    """
A hospital.
    """
    class_: Literal['https://schema.org/Hospital'] = Field(default='https://schema.org/Hospital', alias='class', serialization_alias='class') # type: ignore
    healthcareReportingData: Optional[Union[Dataset, List[Dataset], "CDCPMDRecord", List["CDCPMDRecord"]]] = Field(default=None, validation_alias=AliasChoices('healthcareReportingData', 'https://schema.org/healthcareReportingData'), serialization_alias='https://schema.org/healthcareReportingData')
    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = Field(default=None, validation_alias=AliasChoices('medicalSpecialty', 'https://schema.org/medicalSpecialty'), serialization_alias='https://schema.org/medicalSpecialty')
    availableService: Optional[Union[MedicalProcedure, List[MedicalProcedure], "MedicalTherapy", List["MedicalTherapy"], MedicalTest, List[MedicalTest]]] = Field(default=None, validation_alias=AliasChoices('availableService', 'https://schema.org/availableService'), serialization_alias='https://schema.org/availableService')
