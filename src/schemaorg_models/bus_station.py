from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class BusStation(CivicStructure):
    """
A bus station.
    """
    class_: Literal['https://schema.org/BusStation'] = Field(default='https://schema.org/BusStation', alias='class', serialization_alias='class') # type: ignore
