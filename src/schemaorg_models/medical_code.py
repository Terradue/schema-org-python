from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_intangible import MedicalIntangible


class MedicalCode(MedicalIntangible):
    """
A code for a medical entity.
    """
    class_: Literal['https://schema.org/MedicalCode'] = Field(default='https://schema.org/MedicalCode', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    codingSystem: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('codingSystem', 'https://schema.org/codingSystem'), serialization_alias='https://schema.org/codingSystem')
    codeValue: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('codeValue', 'https://schema.org/codeValue'), serialization_alias='https://schema.org/codeValue')
