from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Museum(CivicStructure):
    """
A museum.
    """
    type_: Literal['https://schema.org/Museum'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Museum'),serialization_alias='class') # type: ignore
