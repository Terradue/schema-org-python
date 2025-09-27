from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PoliceStation(CivicStructure):
    """
A police station.
    """
    type_: Literal['https://schema.org/PoliceStation'] = Field(default='https://schema.org/PoliceStation', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
