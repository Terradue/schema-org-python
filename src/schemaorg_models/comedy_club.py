from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """
A comedy club.
    """
    type_: Literal['https://schema.org/ComedyClub'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ComedyClub'),serialization_alias='class') # type: ignore
