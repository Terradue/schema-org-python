from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class MusicVenue(CivicStructure):
    """
A music venue.
    """
    class_: Literal['https://schema.org/MusicVenue'] = Field('class', alias='class', serialization_alias='class') # type: ignore
