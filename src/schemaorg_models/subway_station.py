from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class SubwayStation(CivicStructure):
    """
A subway station.
    """
    type_: Literal['https://schema.org/SubwayStation'] = Field(default='https://schema.org/SubwayStation', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
