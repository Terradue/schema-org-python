from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class MusicVenue(CivicStructure):
    """
A music venue.
    """
    class_: Literal['https://schema.org/MusicVenue'] = Field(default='https://schema.org/MusicVenue', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
