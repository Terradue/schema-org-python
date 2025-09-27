from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class TelevisionStation(LocalBusiness):
    """
A television station.
    """
    class_: Literal['https://schema.org/TelevisionStation'] = Field(default='https://schema.org/TelevisionStation', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
