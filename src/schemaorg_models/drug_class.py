from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity


class DrugClass(MedicalEntity):
    """
A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.
    """
    type_: Literal['https://schema.org/DrugClass'] = Field(default='https://schema.org/DrugClass', alias='@type', serialization_alias='@type') # type: ignore
    drug: Optional[Union["Drug", List["Drug"]]] = Field(default=None, validation_alias=AliasChoices('drug', 'https://schema.org/drug'), serialization_alias='https://schema.org/drug')
