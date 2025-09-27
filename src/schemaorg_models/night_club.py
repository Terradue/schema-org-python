from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """
A nightclub or discotheque.
    """
    type_: Literal['https://schema.org/NightClub'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/NightClub'),serialization_alias='class') # type: ignore
