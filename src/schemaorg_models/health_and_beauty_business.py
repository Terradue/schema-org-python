from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """
Health and beauty.
    """
    type_: Literal['https://schema.org/HealthAndBeautyBusiness'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HealthAndBeautyBusiness'),serialization_alias='class') # type: ignore
