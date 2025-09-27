from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.create_action import CreateAction

from schemaorg_models.food_event import FoodEvent
from schemaorg_models.recipe import Recipe
from schemaorg_models.place import Place
from schemaorg_models.food_establishment import FoodEstablishment

class CookAction(CreateAction):
    """
The act of producing/preparing food.
    """
    type_: Literal['https://schema.org/CookAction'] = Field(default='https://schema.org/CookAction', alias='@type', serialization_alias='@type') # type: ignore
    foodEvent: Optional[Union[FoodEvent, List[FoodEvent]]] = Field(default=None, validation_alias=AliasChoices('foodEvent', 'https://schema.org/foodEvent'), serialization_alias='https://schema.org/foodEvent')
    recipe: Optional[Union[Recipe, List[Recipe]]] = Field(default=None, validation_alias=AliasChoices('recipe', 'https://schema.org/recipe'), serialization_alias='https://schema.org/recipe')
    foodEstablishment: Optional[Union[Place, List[Place], FoodEstablishment, List[FoodEstablishment]]] = Field(default=None, validation_alias=AliasChoices('foodEstablishment', 'https://schema.org/foodEstablishment'), serialization_alias='https://schema.org/foodEstablishment')
