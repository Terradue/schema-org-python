from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """
A theater or other performing art center.
    """
    class_: Literal['https://schema.org/PerformingArtsTheater'] = Field(default='https://schema.org/PerformingArtsTheater', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
