from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """
A casino.
    """
    type_: Literal['https://schema.org/Casino'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Casino'),serialization_alias='class') # type: ignore
