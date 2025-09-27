from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """
A government building.
    """
    type_: Literal['https://schema.org/GovernmentBuilding'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GovernmentBuilding'),serialization_alias='class') # type: ignore
