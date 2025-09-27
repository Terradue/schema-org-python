from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class ParkingFacility(CivicStructure):
    """
A parking lot or other parking facility.
    """
    type_: Literal['https://schema.org/ParkingFacility'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ParkingFacility'),serialization_alias='class') # type: ignore
