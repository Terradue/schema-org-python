from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class EventVenue(CivicStructure):
    """
An event venue.
    """
    class_: Literal['https://schema.org/EventVenue'] = Field(default='https://schema.org/EventVenue', alias='class', serialization_alias='class') # type: ignore
