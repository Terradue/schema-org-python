from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class FireStation(CivicStructure):
    """
A fire station. With firemen.
    """
    class_: Literal['https://schema.org/FireStation'] = Field('class', alias='class', serialization_alias='class') # type: ignore
