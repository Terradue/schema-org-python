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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .taxon import Taxon
    from .gene import Gene
    from .property_value import PropertyValue
    from .grant import Grant
    from .defined_term import DefinedTerm
    from .medical_condition import MedicalCondition

class BioChemEntity(Thing):
    '''
    Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical; a synthetic chemical.

    Attributes:
        taxonomicRange: The taxonomic grouping of the organism that expresses, encodes, or in some way related to the BioChemEntity.
        isInvolvedInBiologicalProcess: Biological process this BioChemEntity is involved in; please use PropertyValue if you want to include any evidence.
        hasBioChemEntityPart: Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part. 
        bioChemSimilarity: A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.
        hasRepresentation: A common representation such as a protein sequence or chemical structure for this entity. For images use schema.org/image.
        biologicalRole: A role played by the BioChemEntity within a biological context.
        hasMolecularFunction: Molecular function performed by this BioChemEntity; please use PropertyValue if you want to include any evidence.
        bioChemInteraction: A BioChemEntity that is known to interact with this item.
        isLocatedInSubcellularLocation: Subcellular location where this BioChemEntity is located; please use PropertyValue if you want to include any evidence.
        funding: A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        isPartOfBioChemEntity: Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity. 
        isEncodedByBioChemEntity: Another BioChemEntity encoding by this one.
        associatedDisease: Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or a URL. If you want to add an evidence supporting the association, please use PropertyValue.
    '''
    class_: Literal['https://schema.org/BioChemEntity'] = Field( # type: ignore
        default='https://schema.org/BioChemEntity',
        alias='@type',
        serialization_alias='@type'
    )
    taxonomicRange: Optional[Union['Taxon', List['Taxon'], 'DefinedTerm', List['DefinedTerm'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'taxonomicRange',
            'https://schema.org/taxonomicRange'
        ),
        serialization_alias='https://schema.org/taxonomicRange'
    )
    isInvolvedInBiologicalProcess: Optional[Union['PropertyValue', List['PropertyValue'], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isInvolvedInBiologicalProcess',
            'https://schema.org/isInvolvedInBiologicalProcess'
        ),
        serialization_alias='https://schema.org/isInvolvedInBiologicalProcess'
    )
    hasBioChemEntityPart: Optional[Union['BioChemEntity', List['BioChemEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasBioChemEntityPart',
            'https://schema.org/hasBioChemEntityPart'
        ),
        serialization_alias='https://schema.org/hasBioChemEntityPart'
    )
    bioChemSimilarity: Optional[Union['BioChemEntity', List['BioChemEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bioChemSimilarity',
            'https://schema.org/bioChemSimilarity'
        ),
        serialization_alias='https://schema.org/bioChemSimilarity'
    )
    hasRepresentation: Optional[Union['PropertyValue', List['PropertyValue'], HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasRepresentation',
            'https://schema.org/hasRepresentation'
        ),
        serialization_alias='https://schema.org/hasRepresentation'
    )
    biologicalRole: Optional[Union['DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'biologicalRole',
            'https://schema.org/biologicalRole'
        ),
        serialization_alias='https://schema.org/biologicalRole'
    )
    hasMolecularFunction: Optional[Union['PropertyValue', List['PropertyValue'], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMolecularFunction',
            'https://schema.org/hasMolecularFunction'
        ),
        serialization_alias='https://schema.org/hasMolecularFunction'
    )
    bioChemInteraction: Optional[Union['BioChemEntity', List['BioChemEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bioChemInteraction',
            'https://schema.org/bioChemInteraction'
        ),
        serialization_alias='https://schema.org/bioChemInteraction'
    )
    isLocatedInSubcellularLocation: Optional[Union[HttpUrl, List[HttpUrl], 'PropertyValue', List['PropertyValue'], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isLocatedInSubcellularLocation',
            'https://schema.org/isLocatedInSubcellularLocation'
        ),
        serialization_alias='https://schema.org/isLocatedInSubcellularLocation'
    )
    funding: Optional[Union['Grant', List['Grant']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    isPartOfBioChemEntity: Optional[Union['BioChemEntity', List['BioChemEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isPartOfBioChemEntity',
            'https://schema.org/isPartOfBioChemEntity'
        ),
        serialization_alias='https://schema.org/isPartOfBioChemEntity'
    )
    isEncodedByBioChemEntity: Optional[Union['Gene', List['Gene']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isEncodedByBioChemEntity',
            'https://schema.org/isEncodedByBioChemEntity'
        ),
        serialization_alias='https://schema.org/isEncodedByBioChemEntity'
    )
    associatedDisease: Optional[Union['MedicalCondition', List['MedicalCondition'], 'PropertyValue', List['PropertyValue'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedDisease',
            'https://schema.org/associatedDisease'
        ),
        serialization_alias='https://schema.org/associatedDisease'
    )
