from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Park(CivicStructure):
    """
A park.
    """
    type_: Literal['https://schema.org/Park'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Park'),serialization_alias='class') # type: ignore
