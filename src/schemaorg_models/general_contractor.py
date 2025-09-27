from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """
A general contractor.
    """
    class_: Literal['https://schema.org/GeneralContractor'] = Field('class', alias='class', serialization_alias='class') # type: ignore
