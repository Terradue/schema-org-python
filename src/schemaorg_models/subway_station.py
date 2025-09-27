from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class SubwayStation(CivicStructure):
    """
A subway station.
    """
    class_: Literal['https://schema.org/SubwayStation'] = Field('class', alias='class', serialization_alias='class') # type: ignore
