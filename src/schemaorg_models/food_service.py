from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class FoodService(Service):
    """
A food service, like breakfast, lunch, or dinner.
    """
    type_: Literal['https://schema.org/FoodService'] = Field(default='https://schema.org/FoodService', alias='@type', serialization_alias='@type') # type: ignore
