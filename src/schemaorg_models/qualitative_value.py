from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration

from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.enumeration import Enumeration
from schemaorg_models.structured_value import StructuredValue

class QualitativeValue(Enumeration):
    """
A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'.
    """
    type_: Literal['https://schema.org/QualitativeValue'] = Field(default='https://schema.org/QualitativeValue', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    greaterOrEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('greaterOrEqual', 'https://schema.org/greaterOrEqual'), serialization_alias='https://schema.org/greaterOrEqual')
    equal: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('equal', 'https://schema.org/equal'), serialization_alias='https://schema.org/equal')
    lesserOrEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('lesserOrEqual', 'https://schema.org/lesserOrEqual'), serialization_alias='https://schema.org/lesserOrEqual')
    greater: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('greater', 'https://schema.org/greater'), serialization_alias='https://schema.org/greater')
    lesser: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('lesser', 'https://schema.org/lesser'), serialization_alias='https://schema.org/lesser')
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = Field(default=None, validation_alias=AliasChoices('additionalProperty', 'https://schema.org/additionalProperty'), serialization_alias='https://schema.org/additionalProperty')
    valueReference: Optional[Union[DefinedTerm, List[DefinedTerm], "MeasurementTypeEnumeration", List["MeasurementTypeEnumeration"], str, List[str], Enumeration, List[Enumeration], "QualitativeValue", List["QualitativeValue"], "QuantitativeValue", List["QuantitativeValue"], "PropertyValue", List["PropertyValue"], StructuredValue, List[StructuredValue]]] = Field(default=None, validation_alias=AliasChoices('valueReference', 'https://schema.org/valueReference'), serialization_alias='https://schema.org/valueReference')
    nonEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('nonEqual', 'https://schema.org/nonEqual'), serialization_alias='https://schema.org/nonEqual')
