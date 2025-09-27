from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Plumber(HomeAndConstructionBusiness):
    """
A plumbing service.
    """
    class_: Literal['https://schema.org/Plumber'] = Field('class', alias='class', serialization_alias='class') # type: ignore
