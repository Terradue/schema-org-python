from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .enumeration import Enumeration
    from .qualitative_value import QualitativeValue
    from .property_value import PropertyValue
    from .measurement_type_enumeration import MeasurementTypeEnumeration
    from .defined_term import DefinedTerm

class QuantitativeValue(StructuredValue):
    """
 A point value or interval for product characteristics and other purposes.
    """
    class_: Literal['https://schema.org/QuantitativeValue'] = Field( # type: ignore
        default='https://schema.org/QuantitativeValue',
        alias='@type',
        serialization_alias='@type'
    )
    unitText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unitText',
            'https://schema.org/unitText'
        ),
        serialization_alias='https://schema.org/unitText'
    )
    minValue: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'minValue',
            'https://schema.org/minValue'
        ),
        serialization_alias='https://schema.org/minValue'
    )
    value: Optional[Union[float, List[float], "StructuredValue", List["StructuredValue"], bool, List[bool], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'value',
            'https://schema.org/value'
        ),
        serialization_alias='https://schema.org/value'
    )
    maxValue: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maxValue',
            'https://schema.org/maxValue'
        ),
        serialization_alias='https://schema.org/maxValue'
    )
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unitCode',
            'https://schema.org/unitCode'
        ),
        serialization_alias='https://schema.org/unitCode'
    )
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty',
            'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty'
    )
    valueReference: Optional[Union["DefinedTerm", List["DefinedTerm"], "MeasurementTypeEnumeration", List["MeasurementTypeEnumeration"], str, List[str], "Enumeration", List["Enumeration"], "QualitativeValue", List["QualitativeValue"], "QuantitativeValue", List["QuantitativeValue"], "PropertyValue", List["PropertyValue"], "StructuredValue", List["StructuredValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'valueReference',
            'https://schema.org/valueReference'
        ),
        serialization_alias='https://schema.org/valueReference'
    )
