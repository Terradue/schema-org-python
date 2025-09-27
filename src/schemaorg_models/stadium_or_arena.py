from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class StadiumOrArena(CivicStructure):
    """
A stadium.
    """
    type_: Literal['https://schema.org/StadiumOrArena'] = Field(default='https://schema.org/StadiumOrArena', alias='@type', serialization_alias='@type') # type: ignore
