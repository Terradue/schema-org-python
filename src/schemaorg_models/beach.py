from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Beach(CivicStructure):
    """
Beach.
    """
    class_: Literal['https://schema.org/Beach'] = Field('class', alias='class', serialization_alias='class') # type: ignore
