from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """
A theater or other performing art center.
    """
    type_: Literal['https://schema.org/PerformingArtsTheater'] = Field(default='https://schema.org/PerformingArtsTheater', alias='@type', serialization_alias='@type') # type: ignore
