from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class Property(Intangible):
    """
A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.
    """
    class_: Literal['https://schema.org/Property'] = Field(default='https://schema.org/Property', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    supersededBy: Optional[Union["Enumeration", List["Enumeration"], "_Class", List["_Class"], "Property", List["Property"]]] = Field(default=None, validation_alias=AliasChoices('supersededBy', 'https://schema.org/supersededBy'), serialization_alias='https://schema.org/supersededBy')
    rangeIncludes: Optional[Union["_Class", List["_Class"]]] = Field(default=None, validation_alias=AliasChoices('rangeIncludes', 'https://schema.org/rangeIncludes'), serialization_alias='https://schema.org/rangeIncludes')
    inverseOf: Optional[Union["Property", List["Property"]]] = Field(default=None, validation_alias=AliasChoices('inverseOf', 'https://schema.org/inverseOf'), serialization_alias='https://schema.org/inverseOf')
    domainIncludes: Optional[Union["_Class", List["_Class"]]] = Field(default=None, validation_alias=AliasChoices('domainIncludes', 'https://schema.org/domainIncludes'), serialization_alias='https://schema.org/domainIncludes')
