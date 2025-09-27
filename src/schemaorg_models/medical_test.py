from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity


class MedicalTest(MedicalEntity):
    """
Any medical test, typically performed for diagnostic purposes.
    """
    type_: Literal['https://schema.org/MedicalTest'] = Field(default='https://schema.org/MedicalTest', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    affectedBy: Optional[Union["Drug", List["Drug"]]] = Field(default=None, validation_alias=AliasChoices('affectedBy', 'https://schema.org/affectedBy'), serialization_alias='https://schema.org/affectedBy')
    signDetected: Optional[Union["MedicalSign", List["MedicalSign"]]] = Field(default=None, validation_alias=AliasChoices('signDetected', 'https://schema.org/signDetected'), serialization_alias='https://schema.org/signDetected')
    usesDevice: Optional[Union["MedicalDevice", List["MedicalDevice"]]] = Field(default=None, validation_alias=AliasChoices('usesDevice', 'https://schema.org/usesDevice'), serialization_alias='https://schema.org/usesDevice')
    usedToDiagnose: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = Field(default=None, validation_alias=AliasChoices('usedToDiagnose', 'https://schema.org/usedToDiagnose'), serialization_alias='https://schema.org/usedToDiagnose')
    normalRange: Optional[Union["MedicalEnumeration", List["MedicalEnumeration"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('normalRange', 'https://schema.org/normalRange'), serialization_alias='https://schema.org/normalRange')
