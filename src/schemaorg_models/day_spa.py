from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class DaySpa(HealthAndBeautyBusiness):
    """
A day spa.
    """
    type_: Literal['https://schema.org/DaySpa'] = Field(default='https://schema.org/DaySpa', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
