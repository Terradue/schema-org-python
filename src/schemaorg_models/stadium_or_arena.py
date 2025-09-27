from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class StadiumOrArena(CivicStructure):
    """
A stadium.
    """
    class_: Literal['https://schema.org/StadiumOrArena'] = Field(default='https://schema.org/StadiumOrArena', alias='class', serialization_alias='class') # type: ignore
