from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.audience import Audience

from schemaorg_models.medical_condition import MedicalCondition

class PeopleAudience(Audience):
    """
A set of characteristics belonging to people, e.g. who compose an item's target audience.
    """
    type_: Literal['https://schema.org/PeopleAudience'] = Field(default='https://schema.org/PeopleAudience', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    suggestedGender: Optional[Union["GenderType", List["GenderType"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('suggestedGender', 'https://schema.org/suggestedGender'), serialization_alias='https://schema.org/suggestedGender')
    requiredMaxAge: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('requiredMaxAge', 'https://schema.org/requiredMaxAge'), serialization_alias='https://schema.org/requiredMaxAge')
    suggestedAge: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('suggestedAge', 'https://schema.org/suggestedAge'), serialization_alias='https://schema.org/suggestedAge')
    suggestedMinAge: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('suggestedMinAge', 'https://schema.org/suggestedMinAge'), serialization_alias='https://schema.org/suggestedMinAge')
    requiredGender: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('requiredGender', 'https://schema.org/requiredGender'), serialization_alias='https://schema.org/requiredGender')
    suggestedMaxAge: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('suggestedMaxAge', 'https://schema.org/suggestedMaxAge'), serialization_alias='https://schema.org/suggestedMaxAge')
    requiredMinAge: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('requiredMinAge', 'https://schema.org/requiredMinAge'), serialization_alias='https://schema.org/requiredMinAge')
    suggestedMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('suggestedMeasurement', 'https://schema.org/suggestedMeasurement'), serialization_alias='https://schema.org/suggestedMeasurement')
    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(default=None, validation_alias=AliasChoices('healthCondition', 'https://schema.org/healthCondition'), serialization_alias='https://schema.org/healthCondition')
