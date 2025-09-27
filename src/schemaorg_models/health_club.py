from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class HealthClub(HealthAndBeautyBusiness):
    """
A health club.
    """
    type_: Literal['https://schema.org/HealthClub'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HealthClub'),serialization_alias='class') # type: ignore
