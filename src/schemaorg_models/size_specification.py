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
from .qualitative_value import QualitativeValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .size_group_enumeration import SizeGroupEnumeration
    from .size_system_enumeration import SizeSystemEnumeration
    from .quantitative_value import QuantitativeValue
    from .gender_type import GenderType

class SizeSpecification(QualitativeValue):
    '''
    Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]]).

    Attributes:
        suggestedMeasurement: A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.
        sizeSystem: The size system used to identify a product's size. Typically either a standard (for example, "GS1" or "ISO-EN13402"), country code (for example "US" or "JP"), or a measuring system (for example "Metric" or "Imperial").
        suggestedAge: The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.
        sizeGroup: The size group (also known as "size type") for a product's size. Size groups are common in the fashion industry to define size segments and suggested audiences for wearable products. Multiple values can be combined, for example "men's big and tall", "petite maternity" or "regular".
        hasMeasurement: A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle, the gauge of a screw, or the carbon footprint measured for certification by an authority. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        suggestedGender: The suggested gender of the intended person or audience, for example "male", "female", or "unisex".
    '''
    class_: Literal['https://schema.org/SizeSpecification'] = Field( # type: ignore
        default='https://schema.org/SizeSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    suggestedMeasurement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedMeasurement',
            'https://schema.org/suggestedMeasurement'
        ),
        serialization_alias='https://schema.org/suggestedMeasurement'
    )
    sizeSystem: Optional[Union[str, List[str], 'SizeSystemEnumeration', List['SizeSystemEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sizeSystem',
            'https://schema.org/sizeSystem'
        ),
        serialization_alias='https://schema.org/sizeSystem'
    )
    suggestedAge: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedAge',
            'https://schema.org/suggestedAge'
        ),
        serialization_alias='https://schema.org/suggestedAge'
    )
    sizeGroup: Optional[Union['SizeGroupEnumeration', List['SizeGroupEnumeration'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sizeGroup',
            'https://schema.org/sizeGroup'
        ),
        serialization_alias='https://schema.org/sizeGroup'
    )
    hasMeasurement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement',
            'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement'
    )
    suggestedGender: Optional[Union['GenderType', List['GenderType'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedGender',
            'https://schema.org/suggestedGender'
        ),
        serialization_alias='https://schema.org/suggestedGender'
    )
