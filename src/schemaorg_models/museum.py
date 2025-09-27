from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Museum(CivicStructure):
    """
A museum.
    """
    class_: Literal['https://schema.org/Museum'] = Field('class', alias='class', serialization_alias='class') # type: ignore
