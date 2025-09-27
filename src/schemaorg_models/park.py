from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Park(CivicStructure):
    """
A park.
    """
    type_: Literal['https://schema.org/Park'] = Field(default='https://schema.org/Park', alias='@type', serialization_alias='@type') # type: ignore
