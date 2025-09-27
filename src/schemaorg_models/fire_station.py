from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class FireStation(CivicStructure):
    """
A fire station. With firemen.
    """
    type_: Literal['https://schema.org/FireStation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FireStation'),serialization_alias='class') # type: ignore
