from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """
A comedy club.
    """
    type_: Literal['https://schema.org/ComedyClub'] = Field(default='https://schema.org/ComedyClub', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
