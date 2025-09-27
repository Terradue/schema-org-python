from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Beach(CivicStructure):
    """
Beach.
    """
    type_: Literal['https://schema.org/Beach'] = Field(default='https://schema.org/Beach', alias='@type', serialization_alias='@type') # type: ignore
