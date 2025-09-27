from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity

from schemaorg_models.anatomical_structure import AnatomicalStructure
from schemaorg_models.medical_condition import MedicalCondition

class AnatomicalSystem(MedicalEntity):
    """
An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can include circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems.
    """
    class_: Literal['https://schema.org/AnatomicalSystem'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    associatedPathophysiology: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('associatedPathophysiology', 'https://schema.org/associatedPathophysiology'), serialization_alias='https://schema.org/associatedPathophysiology')
    comprisedOf: Optional[Union[AnatomicalStructure, List[AnatomicalStructure], "AnatomicalSystem", List["AnatomicalSystem"]]] = Field(default=None,validation_alias=AliasChoices('comprisedOf', 'https://schema.org/comprisedOf'), serialization_alias='https://schema.org/comprisedOf')
    relatedStructure: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = Field(default=None,validation_alias=AliasChoices('relatedStructure', 'https://schema.org/relatedStructure'), serialization_alias='https://schema.org/relatedStructure')
    relatedCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(default=None,validation_alias=AliasChoices('relatedCondition', 'https://schema.org/relatedCondition'), serialization_alias='https://schema.org/relatedCondition')
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(default=None,validation_alias=AliasChoices('relatedTherapy', 'https://schema.org/relatedTherapy'), serialization_alias='https://schema.org/relatedTherapy')
