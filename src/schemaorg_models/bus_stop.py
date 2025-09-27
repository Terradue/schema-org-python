from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class BusStop(CivicStructure):
    """
A bus stop.
    """
    class_: Literal['https://schema.org/BusStop'] = Field('class', alias='class', serialization_alias='class') # type: ignore
