from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class HairSalon(HealthAndBeautyBusiness):
    """
A hair salon.
    """
    type_: Literal['https://schema.org/HairSalon'] = Field(default='https://schema.org/HairSalon', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
