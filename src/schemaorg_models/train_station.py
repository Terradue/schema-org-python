from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class TrainStation(CivicStructure):
    """
A train station.
    """
    class_: Literal['https://schema.org/TrainStation'] = Field(default='https://schema.org/TrainStation', alias='@type', serialization_alias='@type') # type: ignore
