from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PlaceOfWorship(CivicStructure):
    """
Place of worship, such as a church, synagogue, or mosque.
    """
    type_: Literal['https://schema.org/PlaceOfWorship'] = Field(default='https://schema.org/PlaceOfWorship', alias='@type', serialization_alias='@type') # type: ignore
