from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class AmusementPark(EntertainmentBusiness):
    """
An amusement park.
    """
    type_: Literal['https://schema.org/AmusementPark'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AmusementPark'),serialization_alias='class') # type: ignore
