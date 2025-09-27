from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class BusStation(CivicStructure):
    """
A bus station.
    """
    type_: Literal['https://schema.org/BusStation'] = Field(default='https://schema.org/BusStation', alias='@type', serialization_alias='@type') # type: ignore
