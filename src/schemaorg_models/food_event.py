from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class FoodEvent(Event):
    """
A sub property of location. The specific food event where the action occurred.
    """
    type_: Literal['https://schema.org/FoodEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FoodEvent'),serialization_alias='class') # type: ignore
