from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class BusStop(CivicStructure):
    """
A bus stop.
    """
    type_: Literal['https://schema.org/BusStop'] = Field(default='https://schema.org/BusStop', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
