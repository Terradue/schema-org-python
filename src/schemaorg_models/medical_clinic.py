from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_organization import MedicalOrganization

from schemaorg_models.medical_procedure import MedicalProcedure
from schemaorg_models.medical_test import MedicalTest

class MedicalClinic(MedicalOrganization):
    """
A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.
    """
    type_: Literal['https://schema.org/MedicalClinic'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalClinic'),serialization_alias='class') # type: ignore
    availableService: Optional[Union[MedicalProcedure, List[MedicalProcedure], "MedicalTherapy", List["MedicalTherapy"], MedicalTest, List[MedicalTest]]] = Field(default=None,validation_alias=AliasChoices('availableService', 'https://schema.org/availableService'),serialization_alias='https://schema.org/availableService')
    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = Field(default=None,validation_alias=AliasChoices('medicalSpecialty', 'https://schema.org/medicalSpecialty'),serialization_alias='https://schema.org/medicalSpecialty')
