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
from .recipe import Recipe
from .place import Place
from .food_event import FoodEvent
from .food_establishment import FoodEstablishment
from .create_action import CreateAction

class CookAction(CreateAction):
    """
The act of producing/preparing food.
    """
    class_: Literal['https://schema.org/CookAction'] = Field( # type: ignore
        default='https://schema.org/CookAction',
        alias='@type',
        serialization_alias='@type'
    )
    foodEvent: Optional[Union[FoodEvent, List[FoodEvent]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'foodEvent',
            'https://schema.org/foodEvent'
        ),
        serialization_alias='https://schema.org/foodEvent'
    )
    recipe: Optional[Union[Recipe, List[Recipe]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipe',
            'https://schema.org/recipe'
        ),
        serialization_alias='https://schema.org/recipe'
    )
    foodEstablishment: Optional[Union[Place, List[Place], FoodEstablishment, List[FoodEstablishment]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'foodEstablishment',
            'https://schema.org/foodEstablishment'
        ),
        serialization_alias='https://schema.org/foodEstablishment'
    )
