from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class BusStation(CivicStructure):
    """
A bus station.
    """
    type_: Literal['https://schema.org/BusStation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BusStation'),serialization_alias='class') # type: ignore
