from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Bridge(CivicStructure):
    """
A bridge.
    """
    type_: Literal['https://schema.org/Bridge'] = Field(default='https://schema.org/Bridge', alias='@type', serialization_alias='@type') # type: ignore
