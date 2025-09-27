from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """
A courthouse.
    """
    class_: Literal['https://schema.org/Courthouse'] = Field(default='https://schema.org/Courthouse', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
