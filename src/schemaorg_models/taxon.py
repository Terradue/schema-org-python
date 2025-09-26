from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.thing import Thing


class Taxon(Thing):
    """
A set of organisms asserted to represent a natural cohesive biological unit.
    """
    hasDefinedTerm: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('hasDefinedTerm', 'https://schema.org/hasDefinedTerm'),serialization_alias='https://schema.org/hasDefinedTerm')
    taxonRank: Optional[Union[str, List[str], "PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('taxonRank', 'https://schema.org/taxonRank'),serialization_alias='https://schema.org/taxonRank')
    @field_serializer('taxonRank')
    def taxonRank2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    parentTaxon: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "Taxon", List["Taxon"]]] = Field(default=None,validation_alias=AliasChoices('parentTaxon', 'https://schema.org/parentTaxon'),serialization_alias='https://schema.org/parentTaxon')
    @field_serializer('parentTaxon')
    def parentTaxon2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    childTaxon: Optional[Union["Taxon", List["Taxon"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('childTaxon', 'https://schema.org/childTaxon'),serialization_alias='https://schema.org/childTaxon')
    @field_serializer('childTaxon')
    def childTaxon2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

