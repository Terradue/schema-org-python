from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class SubwayStation(CivicStructure):
    """
A subway station.
    """
    type_: Literal['https://schema.org/SubwayStation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SubwayStation'),serialization_alias='class') # type: ignore
