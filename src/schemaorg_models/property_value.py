from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.measurement_method_enum import MeasurementMethodEnum
from schemaorg_models.structured_value import StructuredValue
from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schemaorg_models.enumeration import Enumeration
from schemaorg_models.qualitative_value import QualitativeValue
from schemaorg_models.quantitative_value import QuantitativeValue

class PropertyValue(StructuredValue):
    """
A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property.\
\
 Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.
    
    """
    type_: Literal['https://schema.org/PropertyValue'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PropertyValue'),serialization_alias='class') # type: ignore
    unitText: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('unitText', 'https://schema.org/unitText'),serialization_alias='https://schema.org/unitText')
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementMethodEnum, List[MeasurementMethodEnum], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementTechnique', 'https://schema.org/measurementTechnique'),serialization_alias='https://schema.org/measurementTechnique')
    @field_serializer('measurementTechnique')
    def measurementTechnique2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    minValue: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('minValue', 'https://schema.org/minValue'),serialization_alias='https://schema.org/minValue')
    propertyID: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('propertyID', 'https://schema.org/propertyID'),serialization_alias='https://schema.org/propertyID')
    @field_serializer('propertyID')
    def propertyID2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    value: Optional[Union[float, List[float], StructuredValue, List[StructuredValue], bool, List[bool], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('value', 'https://schema.org/value'),serialization_alias='https://schema.org/value')
    maxValue: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('maxValue', 'https://schema.org/maxValue'),serialization_alias='https://schema.org/maxValue')
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('unitCode', 'https://schema.org/unitCode'),serialization_alias='https://schema.org/unitCode')
    @field_serializer('unitCode')
    def unitCode2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], MeasurementMethodEnum, List[MeasurementMethodEnum], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementMethod', 'https://schema.org/measurementMethod'),serialization_alias='https://schema.org/measurementMethod')
    @field_serializer('measurementMethod')
    def measurementMethod2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    valueReference: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementTypeEnumeration, List[MeasurementTypeEnumeration], str, List[str], Enumeration, List[Enumeration], QualitativeValue, List[QualitativeValue], QuantitativeValue, List[QuantitativeValue], "PropertyValue", List["PropertyValue"], StructuredValue, List[StructuredValue]]] = Field(default=None,validation_alias=AliasChoices('valueReference', 'https://schema.org/valueReference'),serialization_alias='https://schema.org/valueReference')
