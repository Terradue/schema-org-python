from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class Beach(CivicStructure):
    """
Beach.
    """
    class_: Literal['https://schema.org/Beach'] = Field(default='https://schema.org/Beach', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
