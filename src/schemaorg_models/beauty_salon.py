from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class BeautySalon(HealthAndBeautyBusiness):
    """
Beauty salon.
    """
    class_: Literal['https://schema.org/BeautySalon'] = Field(default='https://schema.org/BeautySalon', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
