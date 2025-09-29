from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_condition import MedicalCondition
    from .gene import Gene
    from .taxon import Taxon
    from .property_value import PropertyValue
    from .grant import Grant
    from .defined_term import DefinedTerm

class BioChemEntity(Thing):
    """
Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical; a synthetic chemical.
    """
    class_: Literal['https://schema.org/BioChemEntity'] = Field( # type: ignore
        default='https://schema.org/BioChemEntity',
        alias='@type',
        serialization_alias='@type'
    )
    taxonomicRange: Optional[Union["Taxon", List["Taxon"], "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'taxonomicRange',
            'https://schema.org/taxonomicRange'
        ),
        serialization_alias='https://schema.org/taxonomicRange'
    )
    isInvolvedInBiologicalProcess: Optional[Union["PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isInvolvedInBiologicalProcess',
            'https://schema.org/isInvolvedInBiologicalProcess'
        ),
        serialization_alias='https://schema.org/isInvolvedInBiologicalProcess'
    )
    hasBioChemEntityPart: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasBioChemEntityPart',
            'https://schema.org/hasBioChemEntityPart'
        ),
        serialization_alias='https://schema.org/hasBioChemEntityPart'
    )
    bioChemSimilarity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bioChemSimilarity',
            'https://schema.org/bioChemSimilarity'
        ),
        serialization_alias='https://schema.org/bioChemSimilarity'
    )
    hasRepresentation: Optional[Union["PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasRepresentation',
            'https://schema.org/hasRepresentation'
        ),
        serialization_alias='https://schema.org/hasRepresentation'
    )
    biologicalRole: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'biologicalRole',
            'https://schema.org/biologicalRole'
        ),
        serialization_alias='https://schema.org/biologicalRole'
    )
    hasMolecularFunction: Optional[Union["PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMolecularFunction',
            'https://schema.org/hasMolecularFunction'
        ),
        serialization_alias='https://schema.org/hasMolecularFunction'
    )
    bioChemInteraction: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bioChemInteraction',
            'https://schema.org/bioChemInteraction'
        ),
        serialization_alias='https://schema.org/bioChemInteraction'
    )
    isLocatedInSubcellularLocation: Optional[Union[HttpUrl, List[HttpUrl], "PropertyValue", List["PropertyValue"], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isLocatedInSubcellularLocation',
            'https://schema.org/isLocatedInSubcellularLocation'
        ),
        serialization_alias='https://schema.org/isLocatedInSubcellularLocation'
    )
    funding: Optional[Union["Grant", List["Grant"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    isPartOfBioChemEntity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isPartOfBioChemEntity',
            'https://schema.org/isPartOfBioChemEntity'
        ),
        serialization_alias='https://schema.org/isPartOfBioChemEntity'
    )
    isEncodedByBioChemEntity: Optional[Union["Gene", List["Gene"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isEncodedByBioChemEntity',
            'https://schema.org/isEncodedByBioChemEntity'
        ),
        serialization_alias='https://schema.org/isEncodedByBioChemEntity'
    )
    associatedDisease: Optional[Union["MedicalCondition", List["MedicalCondition"], "PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedDisease',
            'https://schema.org/associatedDisease'
        ),
        serialization_alias='https://schema.org/associatedDisease'
    )
