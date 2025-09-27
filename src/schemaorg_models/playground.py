from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Playground(CivicStructure):
    """
A playground.
    """
    type_: Literal['https://schema.org/Playground'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Playground'),serialization_alias='class') # type: ignore
