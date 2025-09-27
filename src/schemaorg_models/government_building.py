from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """
A government building.
    """
    type_: Literal['https://schema.org/GovernmentBuilding'] = Field(default='https://schema.org/GovernmentBuilding', alias='@type', serialization_alias='@type') # type: ignore
