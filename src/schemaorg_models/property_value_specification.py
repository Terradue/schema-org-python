from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.thing import Thing

class PropertyValueSpecification(Intangible):
    """
A Property value specification.
    """
    class_: Literal['https://schema.org/PropertyValueSpecification'] = Field(default='https://schema.org/PropertyValueSpecification', alias='@type', serialization_alias='@type') # type: ignore
    valuePattern: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('valuePattern', 'https://schema.org/valuePattern'), serialization_alias='https://schema.org/valuePattern')
    minValue: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('minValue', 'https://schema.org/minValue'), serialization_alias='https://schema.org/minValue')
    stepValue: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('stepValue', 'https://schema.org/stepValue'), serialization_alias='https://schema.org/stepValue')
    readonlyValue: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('readonlyValue', 'https://schema.org/readonlyValue'), serialization_alias='https://schema.org/readonlyValue')
    valueRequired: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('valueRequired', 'https://schema.org/valueRequired'), serialization_alias='https://schema.org/valueRequired')
    maxValue: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('maxValue', 'https://schema.org/maxValue'), serialization_alias='https://schema.org/maxValue')
    defaultValue: Optional[Union[str, List[str], Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('defaultValue', 'https://schema.org/defaultValue'), serialization_alias='https://schema.org/defaultValue')
    valueMinLength: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('valueMinLength', 'https://schema.org/valueMinLength'), serialization_alias='https://schema.org/valueMinLength')
    multipleValues: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('multipleValues', 'https://schema.org/multipleValues'), serialization_alias='https://schema.org/multipleValues')
    valueMaxLength: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('valueMaxLength', 'https://schema.org/valueMaxLength'), serialization_alias='https://schema.org/valueMaxLength')
    valueName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('valueName', 'https://schema.org/valueName'), serialization_alias='https://schema.org/valueName')
