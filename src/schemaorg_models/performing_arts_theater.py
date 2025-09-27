from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """
A theater or other performing art center.
    """
    type_: Literal['https://schema.org/PerformingArtsTheater'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PerformingArtsTheater'),serialization_alias='class') # type: ignore
