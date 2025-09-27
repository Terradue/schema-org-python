from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PoliceStation(CivicStructure):
    """
A police station.
    """
    class_: Literal['https://schema.org/PoliceStation'] = Field('class', alias='class', serialization_alias='class') # type: ignore
