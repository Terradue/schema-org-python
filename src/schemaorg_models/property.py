from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class Property(Intangible):
    """
A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.
    """
    supersededBy: Optional[Union["Enumeration", List["Enumeration"], "_Class", List["_Class"], "Property", List["Property"]]] = Field(default=None,validation_alias=AliasChoices('supersededBy', 'https://schema.org/supersededBy'),serialization_alias='https://schema.org/supersededBy')
    rangeIncludes: Optional[Union["_Class", List["_Class"]]] = Field(default=None,validation_alias=AliasChoices('rangeIncludes', 'https://schema.org/rangeIncludes'),serialization_alias='https://schema.org/rangeIncludes')
    inverseOf: Optional[Union["Property", List["Property"]]] = Field(default=None,validation_alias=AliasChoices('inverseOf', 'https://schema.org/inverseOf'),serialization_alias='https://schema.org/inverseOf')
    domainIncludes: Optional[Union["_Class", List["_Class"]]] = Field(default=None,validation_alias=AliasChoices('domainIncludes', 'https://schema.org/domainIncludes'),serialization_alias='https://schema.org/domainIncludes')
