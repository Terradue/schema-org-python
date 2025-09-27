from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class FoodEvent(Event):
    """
A sub property of location. The specific food event where the action occurred.
    """
    type_: Literal['https://schema.org/FoodEvent'] = Field(default='https://schema.org/FoodEvent', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
