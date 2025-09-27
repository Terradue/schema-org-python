from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class RealEstateAgent(LocalBusiness):
    """
A real-estate agent.
    """
    class_: Literal['https://schema.org/RealEstateAgent'] = Field(default='https://schema.org/RealEstateAgent', alias='@type', serialization_alias='@type') # type: ignore
