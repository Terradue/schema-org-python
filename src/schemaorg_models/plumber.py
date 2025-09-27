from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Plumber(HomeAndConstructionBusiness):
    """
A plumbing service.
    """
    type_: Literal['https://schema.org/Plumber'] = Field(default='https://schema.org/Plumber', alias='@type', serialization_alias='@type') # type: ignore
