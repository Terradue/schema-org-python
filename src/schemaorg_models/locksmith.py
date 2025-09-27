from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Locksmith(HomeAndConstructionBusiness):
    """
A locksmith.
    """
    type_: Literal['https://schema.org/Locksmith'] = Field(default='https://schema.org/Locksmith', alias='@type', serialization_alias='@type') # type: ignore
