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
from .enumeration import Enumeration
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .measurement_type_enumeration import MeasurementTypeEnumeration
    from .property_value import PropertyValue
    from .structured_value import StructuredValue
    from .defined_term import DefinedTerm
    from .quantitative_value import QuantitativeValue

class QualitativeValue(Enumeration):
    '''
    A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'.

    Attributes:
        greaterOrEqual: This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.
        equal: This ordering relation for qualitative values indicates that the subject is equal to the object.
        lesserOrEqual: This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.
        greater: This ordering relation for qualitative values indicates that the subject is greater than the object.
        lesser: This ordering relation for qualitative values indicates that the subject is lesser than the object.
        additionalProperty: A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.\
\
Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

        valueReference: A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.
        nonEqual: This ordering relation for qualitative values indicates that the subject is not equal to the object.
    '''
    class_: Literal['https://schema.org/QualitativeValue'] = Field( # type: ignore
        default='https://schema.org/QualitativeValue',
        alias='@type',
        serialization_alias='@type'
    )
    greaterOrEqual: Optional[Union['QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'greaterOrEqual',
            'https://schema.org/greaterOrEqual'
        ),
        serialization_alias='https://schema.org/greaterOrEqual'
    )
    equal: Optional[Union['QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'equal',
            'https://schema.org/equal'
        ),
        serialization_alias='https://schema.org/equal'
    )
    lesserOrEqual: Optional[Union['QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lesserOrEqual',
            'https://schema.org/lesserOrEqual'
        ),
        serialization_alias='https://schema.org/lesserOrEqual'
    )
    greater: Optional[Union['QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'greater',
            'https://schema.org/greater'
        ),
        serialization_alias='https://schema.org/greater'
    )
    lesser: Optional[Union['QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lesser',
            'https://schema.org/lesser'
        ),
        serialization_alias='https://schema.org/lesser'
    )
    additionalProperty: Optional[Union['PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty',
            'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty'
    )
    valueReference: Optional[Union['DefinedTerm', List['DefinedTerm'], 'MeasurementTypeEnumeration', List['MeasurementTypeEnumeration'], str, List[str], 'Enumeration', List['Enumeration'], 'QualitativeValue', List['QualitativeValue'], 'QuantitativeValue', List['QuantitativeValue'], 'PropertyValue', List['PropertyValue'], 'StructuredValue', List['StructuredValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'valueReference',
            'https://schema.org/valueReference'
        ),
        serialization_alias='https://schema.org/valueReference'
    )
    nonEqual: Optional[Union['QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nonEqual',
            'https://schema.org/nonEqual'
        ),
        serialization_alias='https://schema.org/nonEqual'
    )
