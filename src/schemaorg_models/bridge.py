from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Bridge(CivicStructure):
    """
A bridge.
    """
    type_: Literal['https://schema.org/Bridge'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Bridge'),serialization_alias='class') # type: ignore
