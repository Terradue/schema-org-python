from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_intangible import MedicalIntangible


class MedicalCode(MedicalIntangible):
    """
A code for a medical entity.
    """
    type_: Literal['https://schema.org/MedicalCode'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalCode'),serialization_alias='class') # type: ignore
    codingSystem: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('codingSystem', 'https://schema.org/codingSystem'),serialization_alias='https://schema.org/codingSystem')
    codeValue: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('codeValue', 'https://schema.org/codeValue'),serialization_alias='https://schema.org/codeValue')
