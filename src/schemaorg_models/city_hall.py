from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """
A city hall.
    """
    type_: Literal['https://schema.org/CityHall'] = Field(default='https://schema.org/CityHall', alias='@type', serialization_alias='@type') # type: ignore
