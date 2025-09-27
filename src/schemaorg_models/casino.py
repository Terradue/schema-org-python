from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """
A casino.
    """
    class_: Literal['https://schema.org/Casino'] = Field(default='https://schema.org/Casino', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
