from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.structured_value import StructuredValue
from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schemaorg_models.enumeration import Enumeration
from schemaorg_models.qualitative_value import QualitativeValue

class QuantitativeValue(StructuredValue):
    """
 A point value or interval for product characteristics and other purposes.
    """
    type_: Literal['https://schema.org/QuantitativeValue'] = Field(default='https://schema.org/QuantitativeValue', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    unitText: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('unitText', 'https://schema.org/unitText'), serialization_alias='https://schema.org/unitText')
    minValue: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('minValue', 'https://schema.org/minValue'), serialization_alias='https://schema.org/minValue')
    value: Optional[Union[float, List[float], StructuredValue, List[StructuredValue], bool, List[bool], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('value', 'https://schema.org/value'), serialization_alias='https://schema.org/value')
    maxValue: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('maxValue', 'https://schema.org/maxValue'), serialization_alias='https://schema.org/maxValue')
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('unitCode', 'https://schema.org/unitCode'), serialization_alias='https://schema.org/unitCode')
    @field_serializer('unitCode')
    def unitCode2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = Field(default=None, validation_alias=AliasChoices('additionalProperty', 'https://schema.org/additionalProperty'), serialization_alias='https://schema.org/additionalProperty')
    valueReference: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementTypeEnumeration, List[MeasurementTypeEnumeration], str, List[str], Enumeration, List[Enumeration], QualitativeValue, List[QualitativeValue], "QuantitativeValue", List["QuantitativeValue"], "PropertyValue", List["PropertyValue"], StructuredValue, List[StructuredValue]]] = Field(default=None, validation_alias=AliasChoices('valueReference', 'https://schema.org/valueReference'), serialization_alias='https://schema.org/valueReference')
