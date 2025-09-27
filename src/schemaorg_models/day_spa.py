from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class DaySpa(HealthAndBeautyBusiness):
    """
A day spa.
    """
    class_: Literal['https://schema.org/DaySpa'] = Field('class', alias='class', serialization_alias='class') # type: ignore
