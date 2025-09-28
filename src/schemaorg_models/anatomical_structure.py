from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_entity import MedicalEntity

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

class AnatomicalStructure(MedicalEntity):
    """
Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.
    """
    class_: Literal['https://schema.org/AnatomicalStructure'] = Field( # type: ignore
        default='https://schema.org/AnatomicalStructure',
        alias='@type',
        serialization_alias='@type'
    )
    subStructure: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"]]] = Field(
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
    diagram: Optional[Union["ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diagram',
            'https://schema.org/diagram'
        ),
        serialization_alias='https://schema.org/diagram'
    )
    relatedCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(
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
    connectedTo: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'connectedTo',
            'https://schema.org/connectedTo'
        ),
        serialization_alias='https://schema.org/connectedTo'
    )
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedTherapy',
            'https://schema.org/relatedTherapy'
        ),
        serialization_alias='https://schema.org/relatedTherapy'
    )
    partOfSystem: Optional[Union["AnatomicalSystem", List["AnatomicalSystem"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSystem',
            'https://schema.org/partOfSystem'
        ),
        serialization_alias='https://schema.org/partOfSystem'
    )
