from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class HousePainter(HomeAndConstructionBusiness):
    """
A house painting service.
    """
    type_: Literal['https://schema.org/HousePainter'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HousePainter'),serialization_alias='class') # type: ignore
