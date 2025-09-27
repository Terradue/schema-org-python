from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """
An adult entertainment establishment.
    """
    type_: Literal['https://schema.org/AdultEntertainment'] = Field(default='https://schema.org/AdultEntertainment', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
