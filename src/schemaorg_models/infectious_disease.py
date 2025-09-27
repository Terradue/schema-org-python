from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_condition import MedicalCondition


class InfectiousDisease(MedicalCondition):
    """
An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.
    """
    class_: Literal['https://schema.org/InfectiousDisease'] = Field(default='https://schema.org/InfectiousDisease', alias='class', serialization_alias='class') # type: ignore
    transmissionMethod: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('transmissionMethod', 'https://schema.org/transmissionMethod'), serialization_alias='https://schema.org/transmissionMethod')
    infectiousAgentClass: Optional[Union["InfectiousAgentClass", List["InfectiousAgentClass"]]] = Field(default=None, validation_alias=AliasChoices('infectiousAgentClass', 'https://schema.org/infectiousAgentClass'), serialization_alias='https://schema.org/infectiousAgentClass')
    infectiousAgent: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('infectiousAgent', 'https://schema.org/infectiousAgent'), serialization_alias='https://schema.org/infectiousAgent')
