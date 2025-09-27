from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """
A city hall.
    """
    class_: Literal['https://schema.org/CityHall'] = Field(default='https://schema.org/CityHall', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
