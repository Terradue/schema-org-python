from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Zoo(CivicStructure):
    """
A zoo.
    """
    type_: Literal['https://schema.org/Zoo'] = Field(default='https://schema.org/Zoo', alias='@type', serialization_alias='@type') # type: ignore
