from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.health_and_beauty_business import HealthAndBeautyBusiness


class TattooParlor(HealthAndBeautyBusiness):
    """
A tattoo parlor.
    """
    type_: Literal['https://schema.org/TattooParlor'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TattooParlor'),serialization_alias='class') # type: ignore
