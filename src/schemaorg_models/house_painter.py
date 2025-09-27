from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class HousePainter(HomeAndConstructionBusiness):
    """
A house painting service.
    """
    type_: Literal['https://schema.org/HousePainter'] = Field(default='https://schema.org/HousePainter', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
