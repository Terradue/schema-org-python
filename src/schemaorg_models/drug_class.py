from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity


class DrugClass(MedicalEntity):
    """
A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.
    """
    class_: Literal['https://schema.org/DrugClass'] = Field(default='https://schema.org/DrugClass', alias='class', serialization_alias='class') # type: ignore
    drug: Optional[Union["Drug", List["Drug"]]] = Field(default=None, validation_alias=AliasChoices('drug', 'https://schema.org/drug'), serialization_alias='https://schema.org/drug')
