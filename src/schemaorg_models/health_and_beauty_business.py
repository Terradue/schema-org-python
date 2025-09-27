from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """
Health and beauty.
    """
    class_: Literal['https://schema.org/HealthAndBeautyBusiness'] = Field(default='https://schema.org/HealthAndBeautyBusiness', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
