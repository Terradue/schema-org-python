from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class NailSalon(HealthAndBeautyBusiness):
    """
A nail salon.
    """
    type_: Literal['https://schema.org/NailSalon'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/NailSalon'),serialization_alias='class') # type: ignore
