from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class MovingCompany(HomeAndConstructionBusiness):
    """
A moving company.
    """
    type_: Literal['https://schema.org/MovingCompany'] = Field(default='https://schema.org/MovingCompany', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
