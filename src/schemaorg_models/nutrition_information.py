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
    from .energy import Energy
    from .mass import Mass

class NutritionInformation(StructuredValue):
    '''
    Nutritional information about the recipe.

    Attributes:
        unsaturatedFatContent: The number of grams of unsaturated fat.
        cholesterolContent: The number of milligrams of cholesterol.
        calories: The number of calories.
        transFatContent: The number of grams of trans fat.
        fiberContent: The number of grams of fiber.
        servingSize: The serving size, in terms of the number of volume or mass.
        carbohydrateContent: The number of grams of carbohydrates.
        fatContent: The number of grams of fat.
        sodiumContent: The number of milligrams of sodium.
        sugarContent: The number of grams of sugar.
        saturatedFatContent: The number of grams of saturated fat.
        proteinContent: The number of grams of protein.
    '''
    class_: Literal['https://schema.org/NutritionInformation'] = Field( # type: ignore
        default='https://schema.org/NutritionInformation',
        alias='@type',
        serialization_alias='@type'
    )
    unsaturatedFatContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    cholesterolContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    calories: Optional[Union['Energy', List['Energy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    transFatContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    fiberContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    servingSize: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    carbohydrateContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    fatContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    sodiumContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    sugarContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    saturatedFatContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    proteinContent: Optional[Union['Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
