from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """
A courthouse.
    """
    type_: Literal['https://schema.org/Courthouse'] = Field(default='https://schema.org/Courthouse', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
