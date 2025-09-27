from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Cemetery(CivicStructure):
    """
A graveyard.
    """
    type_: Literal['https://schema.org/Cemetery'] = Field(default='https://schema.org/Cemetery', alias='@type', serialization_alias='@type') # type: ignore
