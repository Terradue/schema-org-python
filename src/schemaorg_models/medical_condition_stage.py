from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_intangible import MedicalIntangible


class MedicalConditionStage(MedicalIntangible):
    """
A stage of a medical condition, such as 'Stage IIIa'.
    """
    stageAsNumber: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('stageAsNumber', 'https://schema.org/stageAsNumber'),serialization_alias='https://schema.org/stageAsNumber')
    subStageSuffix: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('subStageSuffix', 'https://schema.org/subStageSuffix'),serialization_alias='https://schema.org/subStageSuffix')
