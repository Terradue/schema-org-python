from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """
A general contractor.
    """
    type_: Literal['https://schema.org/GeneralContractor'] = Field(default='https://schema.org/GeneralContractor', alias='@type', serialization_alias='@type') # type: ignore
