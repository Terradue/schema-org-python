from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class NailSalon(HealthAndBeautyBusiness):
    """
A nail salon.
    """
    type_: Literal['https://schema.org/NailSalon'] = Field(default='https://schema.org/NailSalon', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
