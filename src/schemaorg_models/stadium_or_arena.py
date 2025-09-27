from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class StadiumOrArena(CivicStructure):
    """
A stadium.
    """
    type_: Literal['https://schema.org/StadiumOrArena'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/StadiumOrArena'),serialization_alias='class') # type: ignore
