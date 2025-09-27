from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Aquarium(CivicStructure):
    """
Aquarium.
    """
    type_: Literal['https://schema.org/Aquarium'] = Field(default='https://schema.org/Aquarium', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
