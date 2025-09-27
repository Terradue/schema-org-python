from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class HealthClub(HealthAndBeautyBusiness):
    """
A health club.
    """
    type_: Literal['https://schema.org/HealthClub'] = Field(default='https://schema.org/HealthClub', alias='@type', serialization_alias='@type') # type: ignore
