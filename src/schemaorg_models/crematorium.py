from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class Crematorium(CivicStructure):
    """
A crematorium.
    """
    type_: Literal['https://schema.org/Crematorium'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Crematorium'),serialization_alias='class') # type: ignore
