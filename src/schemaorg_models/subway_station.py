from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class SubwayStation(CivicStructure):
    """
A subway station.
    """
    class_: Literal['https://schema.org/SubwayStation'] = Field(default='https://schema.org/SubwayStation', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
