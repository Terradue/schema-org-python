from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class HousePainter(HomeAndConstructionBusiness):
    """
A house painting service.
    """
    class_: Literal['https://schema.org/HousePainter'] = Field(default='https://schema.org/HousePainter', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
