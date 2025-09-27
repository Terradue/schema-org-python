from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Aquarium(CivicStructure):
    """
Aquarium.
    """
    type_: Literal['https://schema.org/Aquarium'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Aquarium'),serialization_alias='class') # type: ignore
