from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class MusicVenue(CivicStructure):
    """
A music venue.
    """
    class_: Literal['https://schema.org/MusicVenue'] = Field(default='https://schema.org/MusicVenue', alias='@type', serialization_alias='@type') # type: ignore
