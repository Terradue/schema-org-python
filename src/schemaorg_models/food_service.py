from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class FoodService(Service):
    """
A food service, like breakfast, lunch, or dinner.
    """
    class_: Literal['https://schema.org/FoodService'] = Field('class', alias='class', serialization_alias='class') # type: ignore
