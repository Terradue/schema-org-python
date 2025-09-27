from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.thing import Thing


class MedicalEntity(Thing):
    """
The most generic type of entity related to health and the practice of medicine.
    """
    type_: Literal['https://schema.org/MedicalEntity'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalEntity'),serialization_alias='class') # type: ignore
    code: Optional[Union["MedicalCode", List["MedicalCode"]]] = Field(default=None,validation_alias=AliasChoices('code', 'https://schema.org/code'),serialization_alias='https://schema.org/code')
    guideline: Optional[Union["MedicalGuideline", List["MedicalGuideline"]]] = Field(default=None,validation_alias=AliasChoices('guideline', 'https://schema.org/guideline'),serialization_alias='https://schema.org/guideline')
    legalStatus: Optional[Union["DrugLegalStatus", List["DrugLegalStatus"], "MedicalEnumeration", List["MedicalEnumeration"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('legalStatus', 'https://schema.org/legalStatus'),serialization_alias='https://schema.org/legalStatus')
    recognizingAuthority: Optional[Union["Organization", List["Organization"]]] = Field(default=None,validation_alias=AliasChoices('recognizingAuthority', 'https://schema.org/recognizingAuthority'),serialization_alias='https://schema.org/recognizingAuthority')
    medicineSystem: Optional[Union["MedicineSystem", List["MedicineSystem"]]] = Field(default=None,validation_alias=AliasChoices('medicineSystem', 'https://schema.org/medicineSystem'),serialization_alias='https://schema.org/medicineSystem')
    funding: Optional[Union["Grant", List["Grant"]]] = Field(default=None,validation_alias=AliasChoices('funding', 'https://schema.org/funding'),serialization_alias='https://schema.org/funding')
    relevantSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = Field(default=None,validation_alias=AliasChoices('relevantSpecialty', 'https://schema.org/relevantSpecialty'),serialization_alias='https://schema.org/relevantSpecialty')
    study: Optional[Union["MedicalStudy", List["MedicalStudy"]]] = Field(default=None,validation_alias=AliasChoices('study', 'https://schema.org/study'),serialization_alias='https://schema.org/study')
