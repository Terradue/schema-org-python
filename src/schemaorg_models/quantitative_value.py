from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
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
    from .measurement_type_enumeration import MeasurementTypeEnumeration
    from .enumeration import Enumeration
    from .qualitative_value import QualitativeValue
    from .defined_term import DefinedTerm
    from .property_value import PropertyValue

class QuantitativeValue(StructuredValue):
    '''
     A point value or interval for product characteristics and other purposes.

    Attributes:
        unitText: A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href='unitCode'>unitCode</a>.
        minValue: The lower value of some characteristic or property.
        value: The value of a [[QuantitativeValue]] (including [[Observation]]) or property value node.\
\
* For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is 'Number'.\
* For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'.\
* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\
* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        maxValue: The upper value of some characteristic or property.
        unitCode: The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.
        additionalProperty: A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.\
\
Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

        valueReference: A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.
    '''
    class_: Literal['https://schema.org/QuantitativeValue'] = Field( # type: ignore
        default='https://schema.org/QuantitativeValue',
        alias='@type',
        serialization_alias='@type'
    )
    unitText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    minValue: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    value: Optional[Union[float, List[float], 'StructuredValue', List['StructuredValue'], bool, List[bool], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    maxValue: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    additionalProperty: Optional[Union['PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    valueReference: Optional[Union['DefinedTerm', List['DefinedTerm'], 'MeasurementTypeEnumeration', List['MeasurementTypeEnumeration'], str, List[str], 'Enumeration', List['Enumeration'], 'QualitativeValue', List['QualitativeValue'], 'QuantitativeValue', List['QuantitativeValue'], 'PropertyValue', List['PropertyValue'], 'StructuredValue', List['StructuredValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
