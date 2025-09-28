from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
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
    """
Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]]).
    """
    class_: Literal['https://schema.org/SizeSpecification'] = Field( # type: ignore
        default='https://schema.org/SizeSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    suggestedMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedMeasurement',
            'https://schema.org/suggestedMeasurement'
        ),
        serialization_alias='https://schema.org/suggestedMeasurement'
    )
    sizeSystem: Optional[Union[str, List[str], "SizeSystemEnumeration", List["SizeSystemEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sizeSystem',
            'https://schema.org/sizeSystem'
        ),
        serialization_alias='https://schema.org/sizeSystem'
    )
    suggestedAge: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedAge',
            'https://schema.org/suggestedAge'
        ),
        serialization_alias='https://schema.org/suggestedAge'
    )
    sizeGroup: Optional[Union["SizeGroupEnumeration", List["SizeGroupEnumeration"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sizeGroup',
            'https://schema.org/sizeGroup'
        ),
        serialization_alias='https://schema.org/sizeGroup'
    )
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement',
            'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement'
    )
    suggestedGender: Optional[Union["GenderType", List["GenderType"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedGender',
            'https://schema.org/suggestedGender'
        ),
        serialization_alias='https://schema.org/suggestedGender'
    )
