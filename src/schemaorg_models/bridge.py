from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Bridge(CivicStructure):
    """
A bridge.
    """
    class_: Literal['https://schema.org/Bridge'] = Field('class', alias='class', serialization_alias='class') # type: ignore
