from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class BeautySalon(HealthAndBeautyBusiness):
    """
Beauty salon.
    """
    type_: Literal['https://schema.org/BeautySalon'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BeautySalon'),serialization_alias='class') # type: ignore
