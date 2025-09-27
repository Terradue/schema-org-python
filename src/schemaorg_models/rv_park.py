from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class RVPark(CivicStructure):
    """
A place offering space for "Recreational Vehicles", Caravans, mobile homes and the like.
    """
    class_: Literal['https://schema.org/RVPark'] = Field(default='https://schema.org/RVPark', alias='@type', serialization_alias='@type') # type: ignore
