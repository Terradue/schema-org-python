from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class HairSalon(HealthAndBeautyBusiness):
    """
A hair salon.
    """
    type_: Literal['https://schema.org/HairSalon'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HairSalon'),serialization_alias='class') # type: ignore
