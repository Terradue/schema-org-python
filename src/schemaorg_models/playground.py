from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Playground(CivicStructure):
    """
A playground.
    """
    class_: Literal['https://schema.org/Playground'] = Field(default='https://schema.org/Playground', alias='@type', serialization_alias='@type') # type: ignore
