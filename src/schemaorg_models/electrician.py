from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Electrician(HomeAndConstructionBusiness):
    """
An electrician.
    """
    class_: Literal['https://schema.org/Electrician'] = Field(default='https://schema.org/Electrician', alias='class', serialization_alias='class') # type: ignore
