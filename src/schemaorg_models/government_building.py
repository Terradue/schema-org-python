from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """
A government building.
    """
    class_: Literal['https://schema.org/GovernmentBuilding'] = Field(default='https://schema.org/GovernmentBuilding', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
