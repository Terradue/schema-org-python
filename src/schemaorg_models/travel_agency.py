from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class TravelAgency(LocalBusiness):
    """
A travel agency.
    """
    type_: Literal['https://schema.org/TravelAgency'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TravelAgency'),serialization_alias='class') # type: ignore
