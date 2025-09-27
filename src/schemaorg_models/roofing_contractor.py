from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class RoofingContractor(HomeAndConstructionBusiness):
    """
A roofing contractor.
    """
    type_: Literal['https://schema.org/RoofingContractor'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RoofingContractor'),serialization_alias='class') # type: ignore
