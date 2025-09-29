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
    from .anatomical_structure import AnatomicalStructure
    from .medical_condition import MedicalCondition

class AnatomicalSystem(MedicalEntity):
    '''
    An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can include circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems.

    Attributes:
        associatedPathophysiology: If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.
        comprisedOf: Specifying something physically contained by something else. Typically used here for the underlying anatomical structures, such as organs, that comprise the anatomical system.
        relatedStructure: Related anatomical structure(s) that are not part of the system but relate or connect to it, such as vascular bundles associated with an organ system.
        relatedCondition: A medical condition associated with this anatomy.
        relatedTherapy: A medical therapy related to this anatomy.
    '''
    class_: Literal['https://schema.org/AnatomicalSystem'] = Field( # type: ignore
        default='https://schema.org/AnatomicalSystem',
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
    comprisedOf: Optional[Union['AnatomicalStructure', List['AnatomicalStructure'], 'AnatomicalSystem', List['AnatomicalSystem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    relatedStructure: Optional[Union['AnatomicalStructure', List['AnatomicalStructure']]] = Field(
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
