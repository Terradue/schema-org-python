from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Playground(CivicStructure):
    """
A playground.
    """
    class_: Literal['https://schema.org/Playground'] = Field('class', alias='class', serialization_alias='class') # type: ignore
