from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class ParkingFacility(CivicStructure):
    """
A parking lot or other parking facility.
    """
    class_: Literal['https://schema.org/ParkingFacility'] = Field('class', alias='class', serialization_alias='class') # type: ignore
