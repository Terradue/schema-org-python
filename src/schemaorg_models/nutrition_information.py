from __future__ import annotations

from .structured_value import StructuredValue    

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

class NutritionInformation(StructuredValue):
    """
Nutritional information about the recipe.
    """
    class_: Literal['https://schema.org/NutritionInformation'] = Field( # type: ignore
        default='https://schema.org/NutritionInformation',
        alias='@type',
        serialization_alias='@type'
    )
    unsaturatedFatContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unsaturatedFatContent',
            'https://schema.org/unsaturatedFatContent'
        ),
        serialization_alias='https://schema.org/unsaturatedFatContent'
    )
    cholesterolContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cholesterolContent',
            'https://schema.org/cholesterolContent'
        ),
        serialization_alias='https://schema.org/cholesterolContent'
    )
    calories: Optional[Union["Energy", List["Energy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'calories',
            'https://schema.org/calories'
        ),
        serialization_alias='https://schema.org/calories'
    )
    transFatContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transFatContent',
            'https://schema.org/transFatContent'
        ),
        serialization_alias='https://schema.org/transFatContent'
    )
    fiberContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fiberContent',
            'https://schema.org/fiberContent'
        ),
        serialization_alias='https://schema.org/fiberContent'
    )
    servingSize: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'servingSize',
            'https://schema.org/servingSize'
        ),
        serialization_alias='https://schema.org/servingSize'
    )
    carbohydrateContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'carbohydrateContent',
            'https://schema.org/carbohydrateContent'
        ),
        serialization_alias='https://schema.org/carbohydrateContent'
    )
    fatContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fatContent',
            'https://schema.org/fatContent'
        ),
        serialization_alias='https://schema.org/fatContent'
    )
    sodiumContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sodiumContent',
            'https://schema.org/sodiumContent'
        ),
        serialization_alias='https://schema.org/sodiumContent'
    )
    sugarContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sugarContent',
            'https://schema.org/sugarContent'
        ),
        serialization_alias='https://schema.org/sugarContent'
    )
    saturatedFatContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'saturatedFatContent',
            'https://schema.org/saturatedFatContent'
        ),
        serialization_alias='https://schema.org/saturatedFatContent'
    )
    proteinContent: Optional[Union["Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'proteinContent',
            'https://schema.org/proteinContent'
        ),
        serialization_alias='https://schema.org/proteinContent'
    )
