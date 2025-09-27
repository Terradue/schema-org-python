from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class MovingCompany(HomeAndConstructionBusiness):
    """
A moving company.
    """
    class_: Literal['https://schema.org/MovingCompany'] = Field('class', alias='class', serialization_alias='class') # type: ignore
