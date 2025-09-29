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
    from .medical_condition import MedicalCondition
    from .anatomical_system import AnatomicalSystem
    from .medical_therapy import MedicalTherapy
    from .image_object import ImageObject

class AnatomicalStructure(MedicalEntity):
    '''
    Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.

    Attributes:
        subStructure: Component (sub-)structure(s) that comprise this anatomical structure.
        associatedPathophysiology: If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.
        diagram: An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.
        relatedCondition: A medical condition associated with this anatomy.
        bodyLocation: Location in the body of the anatomical structure.
        connectedTo: Other anatomical structures to which this structure is connected.
        relatedTherapy: A medical therapy related to this anatomy.
        partOfSystem: The anatomical or organ system that this structure is part of.
    '''
    class_: Literal['https://schema.org/AnatomicalStructure'] = Field( # type: ignore
        default='https://schema.org/AnatomicalStructure',
        alias='@type',
        serialization_alias='@type'
    )
    subStructure: Optional[Union['AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subStructure',
            'https://schema.org/subStructure'
        ),
        serialization_alias='https://schema.org/subStructure'
    )
    associatedPathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedPathophysiology',
            'https://schema.org/associatedPathophysiology'
        ),
        serialization_alias='https://schema.org/associatedPathophysiology'
    )
    diagram: Optional[Union['ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diagram',
            'https://schema.org/diagram'
        ),
        serialization_alias='https://schema.org/diagram'
    )
    relatedCondition: Optional[Union['MedicalCondition', List['MedicalCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedCondition',
            'https://schema.org/relatedCondition'
        ),
        serialization_alias='https://schema.org/relatedCondition'
    )
    bodyLocation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bodyLocation',
            'https://schema.org/bodyLocation'
        ),
        serialization_alias='https://schema.org/bodyLocation'
    )
    connectedTo: Optional[Union['AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'connectedTo',
            'https://schema.org/connectedTo'
        ),
        serialization_alias='https://schema.org/connectedTo'
    )
    relatedTherapy: Optional[Union['MedicalTherapy', List['MedicalTherapy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedTherapy',
            'https://schema.org/relatedTherapy'
        ),
        serialization_alias='https://schema.org/relatedTherapy'
    )
    partOfSystem: Optional[Union['AnatomicalSystem', List['AnatomicalSystem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSystem',
            'https://schema.org/partOfSystem'
        ),
        serialization_alias='https://schema.org/partOfSystem'
    )
