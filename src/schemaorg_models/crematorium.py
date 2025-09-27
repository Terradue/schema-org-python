from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Crematorium(CivicStructure):
    """
A crematorium.
    """
    class_: Literal['https://schema.org/Crematorium'] = Field(default='https://schema.org/Crematorium', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
