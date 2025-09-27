from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class PoliceStation(CivicStructure):
    """
A police station.
    """
    type_: Literal['https://schema.org/PoliceStation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PoliceStation'),serialization_alias='class') # type: ignore
