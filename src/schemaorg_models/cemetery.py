from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Cemetery(CivicStructure):
    """
A graveyard.
    """
    type_: Literal['https://schema.org/Cemetery'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Cemetery'),serialization_alias='class') # type: ignore
