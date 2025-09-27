from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Park(CivicStructure):
    """
A park.
    """
    class_: Literal['https://schema.org/Park'] = Field('class', alias='class', serialization_alias='class') # type: ignore
