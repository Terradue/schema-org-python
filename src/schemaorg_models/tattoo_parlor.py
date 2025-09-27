from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class TattooParlor(HealthAndBeautyBusiness):
    """
A tattoo parlor.
    """
    type_: Literal['https://schema.org/TattooParlor'] = Field(default='https://schema.org/TattooParlor', alias='@type', serialization_alias='@type') # type: ignore
