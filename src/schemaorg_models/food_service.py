from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.service import Service


class FoodService(Service):
    """
A food service, like breakfast, lunch, or dinner.
    """
    type_: Literal['https://schema.org/FoodService'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FoodService'),serialization_alias='class') # type: ignore
