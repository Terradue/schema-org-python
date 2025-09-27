from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.thing import Thing


class Taxon(Thing):
    """
A set of organisms asserted to represent a natural cohesive biological unit.
    """
    type_: Literal['https://schema.org/Taxon'] = Field(default='https://schema.org/Taxon', alias='@type', serialization_alias='@type') # type: ignore
    hasDefinedTerm: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = Field(default=None, validation_alias=AliasChoices('hasDefinedTerm', 'https://schema.org/hasDefinedTerm'), serialization_alias='https://schema.org/hasDefinedTerm')
    taxonRank: Optional[Union[str, List[str], "PropertyValue", List["PropertyValue"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('taxonRank', 'https://schema.org/taxonRank'), serialization_alias='https://schema.org/taxonRank')
    @field_serializer('taxonRank')
    def taxonRank2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    parentTaxon: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "Taxon", List["Taxon"]]] = Field(default=None, validation_alias=AliasChoices('parentTaxon', 'https://schema.org/parentTaxon'), serialization_alias='https://schema.org/parentTaxon')
    @field_serializer('parentTaxon')
    def parentTaxon2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    childTaxon: Optional[Union["Taxon", List["Taxon"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('childTaxon', 'https://schema.org/childTaxon'), serialization_alias='https://schema.org/childTaxon')
    @field_serializer('childTaxon')
    def childTaxon2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

