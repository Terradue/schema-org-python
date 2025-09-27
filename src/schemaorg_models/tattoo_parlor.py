from typing import Literal
from pydantic import Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class TattooParlor(HealthAndBeautyBusiness):
    """
A tattoo parlor.
    """
    class_: Literal['https://schema.org/TattooParlor'] = Field('class', alias='class', serialization_alias='class') # type: ignore
