from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """
A comedy club.
    """
    class_: Literal['https://schema.org/ComedyClub'] = Field(default='https://schema.org/ComedyClub', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
