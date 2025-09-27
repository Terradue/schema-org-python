from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class RealEstateAgent(LocalBusiness):
    """
A real-estate agent.
    """
    type_: Literal['https://schema.org/RealEstateAgent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RealEstateAgent'),serialization_alias='class') # type: ignore
