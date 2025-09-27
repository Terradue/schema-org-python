from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Beach(CivicStructure):
    """
Beach.
    """
    type_: Literal['https://schema.org/Beach'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Beach'),serialization_alias='class') # type: ignore
