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
from .how_to import HowTo
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .restricted_diet import RestrictedDiet
    from .nutrition_information import NutritionInformation
    from .creative_work import CreativeWork
    from .item_list import ItemList
    from .duration import Duration
    from .property_value import PropertyValue

class Recipe(HowTo):
    '''
    A recipe. For dietary restrictions covered by the recipe, a few common restrictions are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used to add more detail.

    Attributes:
        suitableForDiet: Indicates a dietary restriction or guideline for which this recipe or menu item is suitable, e.g. diabetic, halal etc.
        cookTime: The time it takes to actually cook the dish, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        recipeIngredient: An ingredient or ordered list of ingredients and potentially quantities used in the recipe, e.g. 1 cup of sugar, flour or garlic.  The ingredients can be represented as free text or more structured values.
        recipeInstructions: A step in making the recipe, in the form of a single item (document, video, etc.) or an ordered list with HowToStep and/or HowToSection items.
        recipeYield: The quantity produced by the recipe (for example, number of people served, number of servings, etc).
        ingredients: A single ingredient used in the recipe, e.g. sugar, flour or garlic.
        recipeCategory: The category of the recipe—for example, appetizer, entree, etc.
        nutrition: Nutrition information about the recipe or menu item.
        cookingMethod: The method of cooking, such as Frying, Steaming, ...
        recipeCuisine: The cuisine of the recipe (for example, French or Ethiopian).
    '''
    class_: Literal['https://schema.org/Recipe'] = Field( # type: ignore
        default='https://schema.org/Recipe',
        alias='@type',
        serialization_alias='@type'
    )
    suitableForDiet: Optional[Union['RestrictedDiet', List['RestrictedDiet']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suitableForDiet',
            'https://schema.org/suitableForDiet'
        ),
        serialization_alias='https://schema.org/suitableForDiet'
    )
    cookTime: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cookTime',
            'https://schema.org/cookTime'
        ),
        serialization_alias='https://schema.org/cookTime'
    )
    recipeIngredient: Optional[Union['PropertyValue', List['PropertyValue'], 'ItemList', List['ItemList'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipeIngredient',
            'https://schema.org/recipeIngredient'
        ),
        serialization_alias='https://schema.org/recipeIngredient'
    )
    recipeInstructions: Optional[Union['ItemList', List['ItemList'], str, List[str], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipeInstructions',
            'https://schema.org/recipeInstructions'
        ),
        serialization_alias='https://schema.org/recipeInstructions'
    )
    recipeYield: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipeYield',
            'https://schema.org/recipeYield'
        ),
        serialization_alias='https://schema.org/recipeYield'
    )
    ingredients: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ingredients',
            'https://schema.org/ingredients'
        ),
        serialization_alias='https://schema.org/ingredients'
    )
    recipeCategory: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipeCategory',
            'https://schema.org/recipeCategory'
        ),
        serialization_alias='https://schema.org/recipeCategory'
    )
    nutrition: Optional[Union['NutritionInformation', List['NutritionInformation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nutrition',
            'https://schema.org/nutrition'
        ),
        serialization_alias='https://schema.org/nutrition'
    )
    cookingMethod: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cookingMethod',
            'https://schema.org/cookingMethod'
        ),
        serialization_alias='https://schema.org/cookingMethod'
    )
    recipeCuisine: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipeCuisine',
            'https://schema.org/recipeCuisine'
        ),
        serialization_alias='https://schema.org/recipeCuisine'
    )
