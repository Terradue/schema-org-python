from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class SubwayStation(CivicStructure):
    """
A subway station.
    """
    type_: Literal['https://schema.org/SubwayStation'] = Field(default='https://schema.org/SubwayStation', alias='@type', serialization_alias='@type') # type: ignore
