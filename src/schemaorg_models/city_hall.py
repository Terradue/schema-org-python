from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """
A city hall.
    """
    class_: Literal['https://schema.org/CityHall'] = Field(default='https://schema.org/CityHall', alias='class', serialization_alias='class') # type: ignore
