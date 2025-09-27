from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PoliceStation(CivicStructure):
    """
A police station.
    """
    type_: Literal['https://schema.org/PoliceStation'] = Field(default='https://schema.org/PoliceStation', alias='@type', serialization_alias='@type') # type: ignore
