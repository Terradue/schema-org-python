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
from .audience import Audience
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_condition import MedicalCondition
    from .quantitative_value import QuantitativeValue
    from .gender_type import GenderType

class PeopleAudience(Audience):
    '''
    A set of characteristics belonging to people, e.g. who compose an item's target audience.

    Attributes:
        suggestedGender: The suggested gender of the intended person or audience, for example "male", "female", or "unisex".
        requiredMaxAge: Audiences defined by a person's maximum age.
        suggestedAge: The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.
        suggestedMinAge: Minimum recommended age in years for the audience or user.
        requiredGender: Audiences defined by a person's gender.
        suggestedMaxAge: Maximum recommended age in years for the audience or user.
        requiredMinAge: Audiences defined by a person's minimum age.
        suggestedMeasurement: A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.
        healthCondition: Specifying the health condition(s) of a patient, medical study, or other target audience.
    '''
    class_: Literal['https://schema.org/PeopleAudience'] = Field( # type: ignore
        default='https://schema.org/PeopleAudience',
        alias='@type',
        serialization_alias='@type'
    )
    suggestedGender: Optional[Union['GenderType', List['GenderType'], str, List[str]]] = Field(
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
    suggestedAge: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
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
    suggestedMeasurement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedMeasurement',
            'https://schema.org/suggestedMeasurement'
        ),
        serialization_alias='https://schema.org/suggestedMeasurement'
    )
    healthCondition: Optional[Union['MedicalCondition', List['MedicalCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthCondition',
            'https://schema.org/healthCondition'
        ),
        serialization_alias='https://schema.org/healthCondition'
    )
