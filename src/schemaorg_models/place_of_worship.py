from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PlaceOfWorship(CivicStructure):
    """
Place of worship, such as a church, synagogue, or mosque.
    """
    class_: Literal['https://schema.org/PlaceOfWorship'] = Field('class', alias='class', serialization_alias='class') # type: ignore
