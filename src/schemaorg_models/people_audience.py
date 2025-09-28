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
from .audience import Audience
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .medical_condition import MedicalCondition
    from .gender_type import GenderType

class PeopleAudience(Audience):
    """
A set of characteristics belonging to people, e.g. who compose an item's target audience.
    """
    class_: Literal['https://schema.org/PeopleAudience'] = Field( # type: ignore
        default='https://schema.org/PeopleAudience',
        alias='@type',
        serialization_alias='@type'
    )
    suggestedGender: Optional[Union["GenderType", List["GenderType"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedGender',
            'https://schema.org/suggestedGender'
        ),
        serialization_alias='https://schema.org/suggestedGender'
    )
    requiredMaxAge: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiredMaxAge',
            'https://schema.org/requiredMaxAge'
        ),
        serialization_alias='https://schema.org/requiredMaxAge'
    )
    suggestedAge: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedAge',
            'https://schema.org/suggestedAge'
        ),
        serialization_alias='https://schema.org/suggestedAge'
    )
    suggestedMinAge: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedMinAge',
            'https://schema.org/suggestedMinAge'
        ),
        serialization_alias='https://schema.org/suggestedMinAge'
    )
    requiredGender: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiredGender',
            'https://schema.org/requiredGender'
        ),
        serialization_alias='https://schema.org/requiredGender'
    )
    suggestedMaxAge: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedMaxAge',
            'https://schema.org/suggestedMaxAge'
        ),
        serialization_alias='https://schema.org/suggestedMaxAge'
    )
    requiredMinAge: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiredMinAge',
            'https://schema.org/requiredMinAge'
        ),
        serialization_alias='https://schema.org/requiredMinAge'
    )
    suggestedMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedMeasurement',
            'https://schema.org/suggestedMeasurement'
        ),
        serialization_alias='https://schema.org/suggestedMeasurement'
    )
    healthCondition: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthCondition',
            'https://schema.org/healthCondition'
        ),
        serialization_alias='https://schema.org/healthCondition'
    )
