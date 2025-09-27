from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """
A comedy club.
    """
    class_: Literal['https://schema.org/ComedyClub'] = Field(default='https://schema.org/ComedyClub', alias='@type', serialization_alias='@type') # type: ignore
