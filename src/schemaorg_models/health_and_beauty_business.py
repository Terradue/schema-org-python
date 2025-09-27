from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """
Health and beauty.
    """
    class_: Literal['https://schema.org/HealthAndBeautyBusiness'] = Field('class', alias='class', serialization_alias='class') # type: ignore
