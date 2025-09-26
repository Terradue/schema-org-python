from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_intangible import MedicalIntangible


class MedicalCode(MedicalIntangible):
    """
A code for a medical entity.
    """
    codingSystem: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('codingSystem', 'https://schema.org/codingSystem'),serialization_alias='https://schema.org/codingSystem')
    codeValue: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('codeValue', 'https://schema.org/codeValue'),serialization_alias='https://schema.org/codeValue')
