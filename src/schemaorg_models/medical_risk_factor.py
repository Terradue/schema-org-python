from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity

from schemaorg_models.medical_entity import MedicalEntity

class MedicalRiskFactor(MedicalEntity):
    """
A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication.
    """
    type_: Literal['https://schema.org/MedicalRiskFactor'] = Field(default='https://schema.org/MedicalRiskFactor', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    increasesRiskOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(default=None, validation_alias=AliasChoices('increasesRiskOf', 'https://schema.org/increasesRiskOf'), serialization_alias='https://schema.org/increasesRiskOf')
