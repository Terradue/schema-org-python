from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.government_building import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """
A city hall.
    """
    type_: Literal['https://schema.org/CityHall'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CityHall'),serialization_alias='class') # type: ignore
