from __future__ import annotations

from .medical_entity import MedicalEntity    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.medical_condition import MedicalCondition

class SuperficialAnatomy(MedicalEntity):
    """
Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures. Superficial anatomy plays an important role in sports medicine, phlebotomy, and other medical specialties as underlying anatomical structures can be identified through surface palpation. For example, during back surgery, superficial anatomy can be used to palpate and count vertebrae to find the site of incision. Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example, the median cubital vein can be located by palpating the borders of the cubital fossa (such as the epicondyles of the humerus) and then looking for the superficial signs of the vein, such as size, prominence, ability to refill after depression, and feel of surrounding tissue support. As another example, in a subluxation (dislocation) of the glenohumeral joint, the bony structure becomes pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing the edges of the scapula to be superficially visible. Here, the superficial anatomy is the visible edges of the scapula, implying the underlying dislocation of the joint (the related anatomical structure).
    """
    class_: Literal['https://schema.org/SuperficialAnatomy'] = Field( # type: ignore
        default='https://schema.org/SuperficialAnatomy',
        alias='@type',
        serialization_alias='@type'
    )
    associatedPathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedPathophysiology',
            'https://schema.org/associatedPathophysiology'
        ),
        serialization_alias='https://schema.org/associatedPathophysiology'
    )
    relatedCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedCondition',
            'https://schema.org/relatedCondition'
        ),
        serialization_alias='https://schema.org/relatedCondition'
    )
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedTherapy',
            'https://schema.org/relatedTherapy'
        ),
        serialization_alias='https://schema.org/relatedTherapy'
    )
    relatedAnatomy: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"], "AnatomicalSystem", List["AnatomicalSystem"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedAnatomy',
            'https://schema.org/relatedAnatomy'
        ),
        serialization_alias='https://schema.org/relatedAnatomy'
    )
    significance: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'significance',
            'https://schema.org/significance'
        ),
        serialization_alias='https://schema.org/significance'
    )
