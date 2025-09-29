from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .medical_entity import MedicalEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_therapy import MedicalTherapy
    from .anatomical_system import AnatomicalSystem
    from .anatomical_structure import AnatomicalStructure
    from .medical_condition import MedicalCondition

class SuperficialAnatomy(MedicalEntity):
    '''
    Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures. Superficial anatomy plays an important role in sports medicine, phlebotomy, and other medical specialties as underlying anatomical structures can be identified through surface palpation. For example, during back surgery, superficial anatomy can be used to palpate and count vertebrae to find the site of incision. Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example, the median cubital vein can be located by palpating the borders of the cubital fossa (such as the epicondyles of the humerus) and then looking for the superficial signs of the vein, such as size, prominence, ability to refill after depression, and feel of surrounding tissue support. As another example, in a subluxation (dislocation) of the glenohumeral joint, the bony structure becomes pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing the edges of the scapula to be superficially visible. Here, the superficial anatomy is the visible edges of the scapula, implying the underlying dislocation of the joint (the related anatomical structure).

    Attributes:
        associatedPathophysiology: If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.
        relatedCondition: A medical condition associated with this anatomy.
        relatedTherapy: A medical therapy related to this anatomy.
        relatedAnatomy: Anatomical systems or structures that relate to the superficial anatomy.
        significance: The significance associated with the superficial anatomy; as an example, how characteristics of the superficial anatomy can suggest underlying medical conditions or courses of treatment.
    '''
    class_: Literal['https://schema.org/SuperficialAnatomy'] = Field( # type: ignore
        default='https://schema.org/SuperficialAnatomy',
        alias='@type',
        serialization_alias='@type'
    )
    associatedPathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    relatedCondition: Optional[Union['MedicalCondition', List['MedicalCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    relatedTherapy: Optional[Union['MedicalTherapy', List['MedicalTherapy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    relatedAnatomy: Optional[Union['AnatomicalStructure', List['AnatomicalStructure'], 'AnatomicalSystem', List['AnatomicalSystem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    significance: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
