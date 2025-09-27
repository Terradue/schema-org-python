from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """
An adult entertainment establishment.
    """
    type_: Literal['https://schema.org/AdultEntertainment'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AdultEntertainment'),serialization_alias='class') # type: ignore
