from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """
A theater or other performing art center.
    """
    class_: Literal['https://schema.org/PerformingArtsTheater'] = Field('class', alias='class', serialization_alias='class') # type: ignore
