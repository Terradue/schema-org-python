from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Electrician(HomeAndConstructionBusiness):
    """
An electrician.
    """
    type_: Literal['https://schema.org/Electrician'] = Field(default='https://schema.org/Electrician', alias='@type', serialization_alias='@type') # type: ignore
