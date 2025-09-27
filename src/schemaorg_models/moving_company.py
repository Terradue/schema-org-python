from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class MovingCompany(HomeAndConstructionBusiness):
    """
A moving company.
    """
    type_: Literal['https://schema.org/MovingCompany'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MovingCompany'),serialization_alias='class') # type: ignore
