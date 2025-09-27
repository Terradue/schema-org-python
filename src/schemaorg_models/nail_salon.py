from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class NailSalon(HealthAndBeautyBusiness):
    """
A nail salon.
    """
    class_: Literal['https://schema.org/NailSalon'] = Field(default='https://schema.org/NailSalon', alias='@type', serialization_alias='@type') # type: ignore
