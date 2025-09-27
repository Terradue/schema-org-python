from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class HVACBusiness(HomeAndConstructionBusiness):
    """
A business that provides Heating, Ventilation and Air Conditioning services.
    """
    class_: Literal['https://schema.org/HVACBusiness'] = Field(default='https://schema.org/HVACBusiness', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
