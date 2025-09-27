from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class RoofingContractor(HomeAndConstructionBusiness):
    """
A roofing contractor.
    """
    class_: Literal['https://schema.org/RoofingContractor'] = Field(default='https://schema.org/RoofingContractor', alias='@type', serialization_alias='@type') # type: ignore
