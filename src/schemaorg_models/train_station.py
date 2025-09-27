from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class TrainStation(CivicStructure):
    """
A train station.
    """
    class_: Literal['https://schema.org/TrainStation'] = Field('class', alias='class', serialization_alias='class') # type: ignore
