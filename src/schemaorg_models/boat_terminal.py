from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class BoatTerminal(CivicStructure):
    """
A terminal for boats, ships, and other water vessels.
    """
    class_: Literal['https://schema.org/BoatTerminal'] = Field('class', alias='class', serialization_alias='class') # type: ignore
