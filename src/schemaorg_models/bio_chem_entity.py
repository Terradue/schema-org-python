from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.thing import Thing

from schemaorg_models.taxon import Taxon

class BioChemEntity(Thing):
    """
Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical; a synthetic chemical.
    """
    taxonomicRange: Optional[Union[Taxon, List[Taxon], "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('taxonomicRange', 'https://schema.org/taxonomicRange'),serialization_alias='https://schema.org/taxonomicRange')
    @field_serializer('taxonomicRange')
    def taxonomicRange2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    isInvolvedInBiologicalProcess: Optional[Union["PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('isInvolvedInBiologicalProcess', 'https://schema.org/isInvolvedInBiologicalProcess'),serialization_alias='https://schema.org/isInvolvedInBiologicalProcess')
    @field_serializer('isInvolvedInBiologicalProcess')
    def isInvolvedInBiologicalProcess2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    hasBioChemEntityPart: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = Field(default=None,validation_alias=AliasChoices('hasBioChemEntityPart', 'https://schema.org/hasBioChemEntityPart'),serialization_alias='https://schema.org/hasBioChemEntityPart')
    bioChemSimilarity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = Field(default=None,validation_alias=AliasChoices('bioChemSimilarity', 'https://schema.org/bioChemSimilarity'),serialization_alias='https://schema.org/bioChemSimilarity')
    hasRepresentation: Optional[Union["PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('hasRepresentation', 'https://schema.org/hasRepresentation'),serialization_alias='https://schema.org/hasRepresentation')
    @field_serializer('hasRepresentation')
    def hasRepresentation2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    biologicalRole: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('biologicalRole', 'https://schema.org/biologicalRole'),serialization_alias='https://schema.org/biologicalRole')
    hasMolecularFunction: Optional[Union["PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('hasMolecularFunction', 'https://schema.org/hasMolecularFunction'),serialization_alias='https://schema.org/hasMolecularFunction')
    @field_serializer('hasMolecularFunction')
    def hasMolecularFunction2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    bioChemInteraction: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = Field(default=None,validation_alias=AliasChoices('bioChemInteraction', 'https://schema.org/bioChemInteraction'),serialization_alias='https://schema.org/bioChemInteraction')
    isLocatedInSubcellularLocation: Optional[Union[HttpUrl, List[HttpUrl], "PropertyValue", List["PropertyValue"], "DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('isLocatedInSubcellularLocation', 'https://schema.org/isLocatedInSubcellularLocation'),serialization_alias='https://schema.org/isLocatedInSubcellularLocation')
    @field_serializer('isLocatedInSubcellularLocation')
    def isLocatedInSubcellularLocation2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    funding: Optional[Union["Grant", List["Grant"]]] = Field(default=None,validation_alias=AliasChoices('funding', 'https://schema.org/funding'),serialization_alias='https://schema.org/funding')
    isPartOfBioChemEntity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = Field(default=None,validation_alias=AliasChoices('isPartOfBioChemEntity', 'https://schema.org/isPartOfBioChemEntity'),serialization_alias='https://schema.org/isPartOfBioChemEntity')
    isEncodedByBioChemEntity: Optional[Union["Gene", List["Gene"]]] = Field(default=None,validation_alias=AliasChoices('isEncodedByBioChemEntity', 'https://schema.org/isEncodedByBioChemEntity'),serialization_alias='https://schema.org/isEncodedByBioChemEntity')
    associatedDisease: Optional[Union["MedicalCondition", List["MedicalCondition"], "PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('associatedDisease', 'https://schema.org/associatedDisease'),serialization_alias='https://schema.org/associatedDisease')
    @field_serializer('associatedDisease')
    def associatedDisease2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

