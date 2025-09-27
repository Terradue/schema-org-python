from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """
A nightclub or discotheque.
    """
    class_: Literal['https://schema.org/NightClub'] = Field('class', alias='class', serialization_alias='class') # type: ignore
