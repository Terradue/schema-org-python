from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class HVACBusiness(HomeAndConstructionBusiness):
    """
A business that provides Heating, Ventilation and Air Conditioning services.
    """
    class_: Literal['https://schema.org/HVACBusiness'] = Field('class', alias='class', serialization_alias='class') # type: ignore
