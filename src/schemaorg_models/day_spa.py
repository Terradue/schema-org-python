from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class DaySpa(HealthAndBeautyBusiness):
    """
A day spa.
    """
    type_: Literal['https://schema.org/DaySpa'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DaySpa'),serialization_alias='class') # type: ignore
