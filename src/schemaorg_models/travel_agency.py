from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class TravelAgency(LocalBusiness):
    """
A travel agency.
    """
    class_: Literal['https://schema.org/TravelAgency'] = Field(default='https://schema.org/TravelAgency', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
