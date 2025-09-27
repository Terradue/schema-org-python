from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """
Health and beauty.
    """
    type_: Literal['https://schema.org/HealthAndBeautyBusiness'] = Field(default='https://schema.org/HealthAndBeautyBusiness', alias='@type', serialization_alias='@type') # type: ignore
