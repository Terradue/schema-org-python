from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class AmusementPark(EntertainmentBusiness):
    """
An amusement park.
    """
    class_: Literal['https://schema.org/AmusementPark'] = Field(default='https://schema.org/AmusementPark', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
