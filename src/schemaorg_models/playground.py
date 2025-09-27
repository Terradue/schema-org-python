from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Playground(CivicStructure):
    """
A playground.
    """
    class_: Literal['https://schema.org/Playground'] = Field(default='https://schema.org/Playground', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
