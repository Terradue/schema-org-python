from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.thing import Thing


class Taxon(Thing):
    """
A set of organisms asserted to represent a natural cohesive biological unit.
    """
    hasDefinedTerm: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('hasDefinedTerm', 'https://schema.org/hasDefinedTerm'),serialization_alias='https://schema.org/hasDefinedTerm')
    taxonRank: Optional[Union[str, List[str], "PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('taxonRank', 'https://schema.org/taxonRank'),serialization_alias='https://schema.org/taxonRank')
    parentTaxon: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "Taxon", List["Taxon"]]] = Field(default=None,validation_alias=AliasChoices('parentTaxon', 'https://schema.org/parentTaxon'),serialization_alias='https://schema.org/parentTaxon')
    childTaxon: Optional[Union["Taxon", List["Taxon"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('childTaxon', 'https://schema.org/childTaxon'),serialization_alias='https://schema.org/childTaxon')
