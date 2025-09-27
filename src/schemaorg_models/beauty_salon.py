from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class BeautySalon(HealthAndBeautyBusiness):
    """
Beauty salon.
    """
    class_: Literal['https://schema.org/BeautySalon'] = Field(default='https://schema.org/BeautySalon', alias='class', serialization_alias='class') # type: ignore
