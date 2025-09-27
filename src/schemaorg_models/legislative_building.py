from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.government_building import GovernmentBuilding


class LegislativeBuilding(GovernmentBuilding):
    """
A legislative building&#x2014;for example, the state capitol.
    """
    type_: Literal['https://schema.org/LegislativeBuilding'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LegislativeBuilding'),serialization_alias='class') # type: ignore
