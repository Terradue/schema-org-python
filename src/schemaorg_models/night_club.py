from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """
A nightclub or discotheque.
    """
    class_: Literal['https://schema.org/NightClub'] = Field(default='https://schema.org/NightClub', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
