from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class BoatTerminal(CivicStructure):
    """
A terminal for boats, ships, and other water vessels.
    """
    type_: Literal['https://schema.org/BoatTerminal'] = Field(default='https://schema.org/BoatTerminal', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
