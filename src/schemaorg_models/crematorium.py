from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Crematorium(CivicStructure):
    """
A crematorium.
    """
    class_: Literal['https://schema.org/Crematorium'] = Field(default='https://schema.org/Crematorium', alias='@type', serialization_alias='@type') # type: ignore
