from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Locksmith(HomeAndConstructionBusiness):
    """
A locksmith.
    """
    class_: Literal['https://schema.org/Locksmith'] = Field(default='https://schema.org/Locksmith', alias='class', serialization_alias='class') # type: ignore
