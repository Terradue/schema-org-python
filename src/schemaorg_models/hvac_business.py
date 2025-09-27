from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class HVACBusiness(HomeAndConstructionBusiness):
    """
A business that provides Heating, Ventilation and Air Conditioning services.
    """
    type_: Literal['https://schema.org/HVACBusiness'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HVACBusiness'),serialization_alias='class') # type: ignore
