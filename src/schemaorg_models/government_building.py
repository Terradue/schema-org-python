from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """
A government building.
    """
    class_: Literal['https://schema.org/GovernmentBuilding'] = Field('class', alias='class', serialization_alias='class') # type: ignore
