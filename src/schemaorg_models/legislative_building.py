from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class LegislativeBuilding(GovernmentBuilding):
    """
A legislative building&#x2014;for example, the state capitol.
    """
    class_: Literal['https://schema.org/LegislativeBuilding'] = Field(default='https://schema.org/LegislativeBuilding', alias='class', serialization_alias='class') # type: ignore
