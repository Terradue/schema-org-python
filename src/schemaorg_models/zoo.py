from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Zoo(CivicStructure):
    """
A zoo.
    """
    type_: Literal['https://schema.org/Zoo'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Zoo'),serialization_alias='class') # type: ignore
