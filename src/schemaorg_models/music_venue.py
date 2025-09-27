from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class MusicVenue(CivicStructure):
    """
A music venue.
    """
    type_: Literal['https://schema.org/MusicVenue'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MusicVenue'),serialization_alias='class') # type: ignore
