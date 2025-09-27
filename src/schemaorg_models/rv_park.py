from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class RVPark(CivicStructure):
    """
A place offering space for "Recreational Vehicles", Caravans, mobile homes and the like.
    """
    type_: Literal['https://schema.org/RVPark'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RVPark'),serialization_alias='class') # type: ignore
