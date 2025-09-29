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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .thing import Thing

class PropertyValueSpecification(Intangible):
    '''
    A Property value specification.

    Attributes:
        valuePattern: Specifies a regular expression for testing literal values according to the HTML spec.
        minValue: The lower value of some characteristic or property.
        stepValue: The stepValue attribute indicates the granularity that is expected (and required) of the value in a PropertyValueSpecification.
        readonlyValue: Whether or not a property is mutable.  Default is false. Specifying this for a property that also has a value makes it act similar to a "hidden" input in an HTML form.
        valueRequired: Whether the property must be filled in to complete the action.  Default is false.
        maxValue: The upper value of some characteristic or property.
        defaultValue: The default value of the input.  For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values.
        valueMinLength: Specifies the minimum allowed range for number of characters in a literal value.
        multipleValues: Whether multiple values are allowed for the property.  Default is false.
        valueMaxLength: Specifies the allowed range for number of characters in a literal value.
        valueName: Indicates the name of the PropertyValueSpecification to be used in URL templates and form encoding in a manner analogous to HTML's input@name.
    '''
    class_: Literal['https://schema.org/PropertyValueSpecification'] = Field( # type: ignore
        default='https://schema.org/PropertyValueSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    valuePattern: Optional[Union[str, List[str]]] = Field(
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
    stepValue: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    readonlyValue: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    valueRequired: Optional[Union[bool, List[bool]]] = Field(
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
    defaultValue: Optional[Union[str, List[str], 'Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    valueMinLength: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    multipleValues: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    valueMaxLength: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    valueName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
