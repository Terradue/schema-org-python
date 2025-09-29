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
from .create_action import CreateAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .food_event import FoodEvent
    from .place import Place
    from .food_establishment import FoodEstablishment
    from .recipe import Recipe

class CookAction(CreateAction):
    '''
    The act of producing/preparing food.

    Attributes:
        foodEvent: A sub property of location. The specific food event where the action occurred.
        recipe: A sub property of instrument. The recipe/instructions used to perform the action.
        foodEstablishment: A sub property of location. The specific food establishment where the action occurred.
    '''
    class_: Literal['https://schema.org/CookAction'] = Field( # type: ignore
        default='https://schema.org/CookAction',
        alias='@type',
        serialization_alias='@type'
    )
    foodEvent: Optional[Union['FoodEvent', List['FoodEvent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    recipe: Optional[Union['Recipe', List['Recipe']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    foodEstablishment: Optional[Union['Place', List['Place'], 'FoodEstablishment', List['FoodEstablishment']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
