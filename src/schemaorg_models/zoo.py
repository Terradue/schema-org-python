from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Zoo(CivicStructure):
    """
A zoo.
    """
    class_: Literal['https://schema.org/Zoo'] = Field(default='https://schema.org/Zoo', alias='class', serialization_alias='class') # type: ignore
