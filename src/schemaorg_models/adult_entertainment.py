from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """
An adult entertainment establishment.
    """
    class_: Literal['https://schema.org/AdultEntertainment'] = Field(default='https://schema.org/AdultEntertainment', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
