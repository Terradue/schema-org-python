from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.government_building import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """
A courthouse.
    """
    type_: Literal['https://schema.org/Courthouse'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Courthouse'),serialization_alias='class') # type: ignore
