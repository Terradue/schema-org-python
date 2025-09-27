from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class EventVenue(CivicStructure):
    """
An event venue.
    """
    type_: Literal['https://schema.org/EventVenue'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EventVenue'),serialization_alias='class') # type: ignore
