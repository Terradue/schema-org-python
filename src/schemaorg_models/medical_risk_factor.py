from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity

from schemaorg_models.medical_entity import MedicalEntity

class MedicalRiskFactor(MedicalEntity):
    """
A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication.
    """
    type_: Literal['https://schema.org/MedicalRiskFactor'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalRiskFactor'),serialization_alias='class') # type: ignore
    increasesRiskOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(default=None,validation_alias=AliasChoices('increasesRiskOf', 'https://schema.org/increasesRiskOf'),serialization_alias='https://schema.org/increasesRiskOf')
