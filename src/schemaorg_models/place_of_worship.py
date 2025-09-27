from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class PlaceOfWorship(CivicStructure):
    """
Place of worship, such as a church, synagogue, or mosque.
    """
    type_: Literal['https://schema.org/PlaceOfWorship'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PlaceOfWorship'),serialization_alias='class') # type: ignore
