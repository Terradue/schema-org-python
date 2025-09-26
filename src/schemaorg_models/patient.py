from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_audience import MedicalAudience

from schemaorg_models.medical_condition import MedicalCondition
from schemaorg_models.drug import Drug

class Patient(MedicalAudience):
    """
A patient is any person recipient of health care services.
    """
    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(default=None,validation_alias=AliasChoices('healthCondition', 'https://schema.org/healthCondition'),serialization_alias='https://schema.org/healthCondition')
    diagnosis: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(default=None,validation_alias=AliasChoices('diagnosis', 'https://schema.org/diagnosis'),serialization_alias='https://schema.org/diagnosis')
    drug: Optional[Union[Drug, List[Drug]]] = Field(default=None,validation_alias=AliasChoices('drug', 'https://schema.org/drug'),serialization_alias='https://schema.org/drug')
