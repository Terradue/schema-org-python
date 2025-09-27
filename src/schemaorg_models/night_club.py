from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """
A nightclub or discotheque.
    """
    type_: Literal['https://schema.org/NightClub'] = Field(default='https://schema.org/NightClub', alias='@type', serialization_alias='@type') # type: ignore
