from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_study import MedicalStudy


class MedicalTrial(MedicalStudy):
    """
A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.
    """
    trialDesign: Optional[Union["MedicalTrialDesign", List["MedicalTrialDesign"]]] = Field(default=None,validation_alias=AliasChoices('trialDesign', 'https://schema.org/trialDesign'),serialization_alias='https://schema.org/trialDesign')
