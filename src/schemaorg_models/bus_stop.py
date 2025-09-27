from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class BusStop(CivicStructure):
    """
A bus stop.
    """
    type_: Literal['https://schema.org/BusStop'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BusStop'),serialization_alias='class') # type: ignore
