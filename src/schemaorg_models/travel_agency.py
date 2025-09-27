from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class TravelAgency(LocalBusiness):
    """
A travel agency.
    """
    class_: Literal['https://schema.org/TravelAgency'] = Field(default='https://schema.org/TravelAgency', alias='@type', serialization_alias='@type') # type: ignore
