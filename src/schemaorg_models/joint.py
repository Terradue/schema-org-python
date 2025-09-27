from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.anatomical_structure import AnatomicalStructure

from schemaorg_models.medical_entity import MedicalEntity

class Joint(AnatomicalStructure):
    """
The anatomical location at which two or more bones make contact.
    """
    type_: Literal['https://schema.org/Joint'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Joint'),serialization_alias='class') # type: ignore
    functionalClass: Optional[Union[MedicalEntity, List[MedicalEntity], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('functionalClass', 'https://schema.org/functionalClass'),serialization_alias='https://schema.org/functionalClass')
    structuralClass: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('structuralClass', 'https://schema.org/structuralClass'),serialization_alias='https://schema.org/structuralClass')
    biomechnicalClass: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('biomechnicalClass', 'https://schema.org/biomechnicalClass'),serialization_alias='https://schema.org/biomechnicalClass')
