from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.how_to import HowTo

from schemaorg_models.restricted_diet import RestrictedDiet
from schemaorg_models.duration import Duration
from schemaorg_models.property_value import PropertyValue
from schemaorg_models.item_list import ItemList
from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.nutrition_information import NutritionInformation

class Recipe(HowTo):
    """
A sub property of instrument. The recipe/instructions used to perform the action.
    """
    class_: Literal['https://schema.org/Recipe'] = Field(default='https://schema.org/Recipe', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    suitableForDiet: Optional[Union[RestrictedDiet, List[RestrictedDiet]]] = Field(default=None, validation_alias=AliasChoices('suitableForDiet', 'https://schema.org/suitableForDiet'), serialization_alias='https://schema.org/suitableForDiet')
    cookTime: Optional[Union[Duration, List[Duration]]] = Field(default=None, validation_alias=AliasChoices('cookTime', 'https://schema.org/cookTime'), serialization_alias='https://schema.org/cookTime')
    recipeIngredient: Optional[Union[PropertyValue, List[PropertyValue], ItemList, List[ItemList], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('recipeIngredient', 'https://schema.org/recipeIngredient'), serialization_alias='https://schema.org/recipeIngredient')
    recipeInstructions: Optional[Union[ItemList, List[ItemList], str, List[str], CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('recipeInstructions', 'https://schema.org/recipeInstructions'), serialization_alias='https://schema.org/recipeInstructions')
    recipeYield: Optional[Union[str, List[str], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('recipeYield', 'https://schema.org/recipeYield'), serialization_alias='https://schema.org/recipeYield')
    ingredients: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('ingredients', 'https://schema.org/ingredients'), serialization_alias='https://schema.org/ingredients')
    recipeCategory: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('recipeCategory', 'https://schema.org/recipeCategory'), serialization_alias='https://schema.org/recipeCategory')
    nutrition: Optional[Union[NutritionInformation, List[NutritionInformation]]] = Field(default=None, validation_alias=AliasChoices('nutrition', 'https://schema.org/nutrition'), serialization_alias='https://schema.org/nutrition')
    cookingMethod: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('cookingMethod', 'https://schema.org/cookingMethod'), serialization_alias='https://schema.org/cookingMethod')
    recipeCuisine: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('recipeCuisine', 'https://schema.org/recipeCuisine'), serialization_alias='https://schema.org/recipeCuisine')
