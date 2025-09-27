from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class BoatTerminal(CivicStructure):
    """
A terminal for boats, ships, and other water vessels.
    """
    type_: Literal['https://schema.org/BoatTerminal'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BoatTerminal'),serialization_alias='class') # type: ignore
